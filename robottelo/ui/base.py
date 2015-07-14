# -*- encoding: utf-8 -*-
"""Base class for all UI operations"""

import logging

from robottelo.common.helpers import escape_search
from robottelo.ui.locators import locators, common_locators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


LOGGER = logging.getLogger(__name__)


class UIError(Exception):
    """Indicates that a UI action could not be done."""


class UINoSuchElementError(UIError):
    """Indicates that UI Element is not found."""


class UIPageSubmitionFailed(Exception):
    """Indicates that UI Page submition Failed."""


class Base(object):
    """Base class for UI"""

    logger = LOGGER

    def __init__(self, browser):
        """Sets up the browser object."""
        self.browser = browser

    def find_element(self, locator):
        """Wrapper around Selenium's WebDriver that allows you to search for an
        element in the web page.

        """
        try:
            _webelement = self.browser.find_element(*locator)
            self.wait_for_ajax()
            if _webelement.is_displayed():
                return _webelement
            else:
                return None
        except NoSuchElementException as err:
            self.logger.debug(
                '%s: Could not locate element %s.',
                type(err).__name__,
                locator[1]
            )
        except TimeoutException as err:
            self.logger.debug(
                'Timeout while waiting for locator "%s": "%s"',
                locator[0],
                locator[1]
            )
        return None

    def search_entity(self, element_name, element_locator, search_key=None,
                      katello=None, timeout=None):
        """Uses the search box to locate an element from a list of elements."""

        search_key = search_key or 'name'
        element = None

        if katello:
            searchbox = self.wait_until_element(common_locators['kt_search'])
            search_button = self.wait_until_element(
                common_locators['kt_search_button'])
        else:
            searchbox = self.wait_until_element(common_locators['search'])
            search_button = self.wait_until_element(
                common_locators['search_button'])

        # Do not proceed if searchbox is not found
        if searchbox is None:
            # For katello, search box should be always present on the page
            # no matter we have entity on the page or not...
            if katello:
                raise UINoSuchElementError('Search box not found.')
            # ...but not for foreman
            return None
        else:
            searchbox.clear()
            if search_button:
                searchbox.send_keys(
                    u'{0} = {1}'.format(
                        search_key, escape_search(element_name))
                )
                search_button.click()
            else:
                searchbox.send_keys(escape_search(element_name))
            if timeout:
                element = self.wait_until_element(
                    (element_locator[0], element_locator[1] % element_name),
                    timeout=timeout,
                )
            else:
                element = self.wait_until_element(
                    (element_locator[0], element_locator[1] % element_name))
        return element

    def handle_alert(self, really):
        """
        Handles any alerts
        """
        if really:
            alert = self.browser.switch_to_alert()
            alert.accept()
        else:
            alert = self.browser.switch_to_alert()
            alert.dismiss()

    def select_deselect_entity(self, filter_key, loc, entity_list):
        """Function to select and deselect entity like OS, Partition Table,
        Arch from selection list or by selecting relevant checkbox.

        """
        for entity in entity_list:
            # Scroll to top
            self.browser.execute_script('window.scroll(0, 0)')
            strategy, value = common_locators['filter']
            txt_field = self.wait_until_element((strategy, value % filter_key))
            if txt_field:
                txt_field.clear()
                txt_field.send_keys(entity)
                strategy, value = loc
                self.click((strategy, value % entity))
            else:
                strategy, value = common_locators['entity_checkbox']
                self.click((strategy, value % entity))

    def configure_entity(self, entity_list, filter_key, tab_locator=None,
                         new_entity_list=None, entity_select=True):
        """Configures entities like orgs, OS, ptable, Archs, Users, Usergroups.

        """
        if entity_list is None:
            entity_list = []
        if new_entity_list is None:
            new_entity_list = []
        if entity_list:
            if tab_locator:
                self.click(tab_locator)
            if entity_select:
                entity_locator = common_locators['entity_select']
            else:
                entity_locator = common_locators['entity_deselect']
            self.select_deselect_entity(
                filter_key, entity_locator, entity_list)
        if new_entity_list:
            if tab_locator:
                self.click(tab_locator)
            entity_locator = common_locators['entity_select']
            self.select_deselect_entity(
                filter_key, entity_locator, new_entity_list)

    def delete_entity(self, name, really, name_locator, del_locator,
                      drop_locator=None, search_key=None):
        """Delete an added entity, handles both with and without dropdown."""
        searched = self.search_entity(
            name, name_locator, search_key=search_key)
        if not searched:
            raise UIError('Could not search the entity "{0}"'.format(name))
        if drop_locator:
            strategy, value = drop_locator
            self.click((strategy, value % name))
        strategy, value = del_locator
        self.click((strategy, value % name))
        self.handle_alert(really)

    def wait_until_element_exists(
            self, locator, timeout=12, poll_frequency=0.5):
        """Wrapper around Selenium's WebDriver that allows you to pause your
        test until an element in the web page is present.

        """
        try:
            element = WebDriverWait(
                self.browser, timeout, poll_frequency
            ).until(expected_conditions.presence_of_element_located(locator))
            self.wait_for_ajax(poll_frequency=poll_frequency)
            return element
        except TimeoutException as err:
            self.logger.debug(
                "%s: Timed out waiting for element '%s' to exists.",
                type(err).__name__,
                locator[1]
            )
            return None

    def wait_until_element(self, locator, timeout=12, poll_frequency=0.5):
        """Wrapper around Selenium's WebDriver that allows you to pause your
        test until an element in the web page is present and visible.

        """
        try:
            element = WebDriverWait(
                self.browser, timeout, poll_frequency
            ).until(expected_conditions.visibility_of_element_located(locator))
            self.wait_for_ajax(poll_frequency=poll_frequency)
            return element
        except TimeoutException as err:
            self.logger.debug(
                "%s: Timed out waiting for element '%s' to display.",
                type(err).__name__,
                locator[1]
            )
            return None

    def wait_until_element_is_clickable(
            self, locator, timeout=12, poll_frequency=0.5):
        """Wrapper around Selenium's WebDriver that allows you to pause your
        test until an element in the web page is present and can be clicked.

        """
        try:
            element = WebDriverWait(
                self.browser, timeout, poll_frequency
            ).until(expected_conditions.element_to_be_clickable(locator))
            self.wait_for_ajax(poll_frequency=poll_frequency)
            if element.get_attribute('disabled') == u'true':
                return None
            return element
        except TimeoutException as err:
            self.logger.debug(
                '%s: Timed out waiting for element "%s" to display or to be '
                'clickable.',
                type(err).__name__,
                locator[1]
            )
            return None

    def ajax_complete(self, driver):
        """
        Checks whether an ajax call is completed.
        """

        jquery_active = False
        angular_active = False

        try:
            jquery_active = driver.execute_script('return jQuery.active') > 0
        except WebDriverException:
            pass

        try:
            angular_active = driver.execute_script(
                'return angular.element(document).injector().get("$http")'
                '.pendingRequests.length') > 0
        except WebDriverException:
            pass

        return not (jquery_active or angular_active)

    def wait_for_ajax(self, timeout=30, poll_frequency=0.5):
        """Waits for an ajax call to complete until timeout."""
        WebDriverWait(
            self.browser, timeout, poll_frequency
        ).until(
            self.ajax_complete, 'Timeout waiting for page to load'
        )

    def scroll_page(self):
        """
        Scrolls page up
        """
        self.browser.execute_script('scroll(350, 0);')

    def scroll_right_pane(self):
        """
        Scrolls right pane down to find the save/submit button
        """
        self.browser.execute_script("$('#panel_main').\
                                    data('jsp').scrollBy(0, 100);")

    def field_update(self, loc_string, newtext):
        """
        Function to replace the existing/default text from textbox
        """
        txt_field = self.find_element(locators[loc_string])
        txt_field.clear()
        txt_field.send_keys(newtext)

    def text_field_update(self, locator, newtext):
        """
        Function to replace text from textbox using a common locator
        """
        txt_field = self.wait_until_element(locator)
        txt_field.clear()
        txt_field.send_keys(newtext)

    def set_parameter(self, param_name, param_value):
        """
        Function to set parameters for different
        entities like OS and Domain
        """
        self.click(common_locators['parameter_tab'])
        self.click(common_locators['add_parameter'])
        if self.wait_until_element(common_locators['parameter_name']):
            pname = self.find_element(common_locators['parameter_name'])
            pname.send_keys(param_name)
        if self.wait_until_element(common_locators['parameter_value']):
            pvalue = self.find_element(common_locators['parameter_value'])
            pvalue.send_keys(param_value)
        self.click(common_locators['submit'])

    def remove_parameter(self, param_name):
        """Function to remove parameters for different entities like OS and
        Domain.

        """
        self.click(common_locators['parameter_tab'])
        strategy, value = common_locators['parameter_remove']
        self.click((strategy, value % param_name))
        self.click(common_locators['submit'])

    def edit_entity(self, edit_loc, edit_text_loc, entity_value, save_loc):
        """Function to edit the selected entity's  text and save it."""
        self.click(edit_loc)
        self.text_field_update(edit_text_loc, entity_value)
        self.click(save_loc)

    def auto_complete_search(self, go_to_page, entity_locator, partial_name,
                             name, search_key):
        """
        Auto complete search by giving partial name of any entity.

        :param go_to_page: Navigates to the entities page.
        :param entity_locator: The locator of the entity.
        :param str partial_name: The partial name of the entity.
        :param str name: The name of the entity. Ex: org, loc
        :param str search_key: The search key for searching an entity. Ex: name
        :return: Returns the searched element.

        """
        go_to_page()
        strategy1, value1 = entity_locator
        searchbox = self.wait_until_element(common_locators['search'])
        if searchbox is None:
            raise UINoSuchElementError('Search box not found.')
        searchbox.clear()
        searchbox.send_keys(search_key + " = " + partial_name)
        self.wait_for_ajax()
        strategy, value = common_locators['auto_search']
        self.click((strategy, value % name))
        self.click(common_locators['search_button'])
        entity_elem = self.wait_until_element((strategy1, value1 % name))
        return entity_elem

    def check_all_values(self, go_to_page, entity_name, entity_locator,
                         tab_locator, context=None):
        """
        Checks whether the 'All values' checkbox is checked/selected.

        :param go_to_page: Navigates to the entities page.
        :param str entity_name: The name of the entity. Ex: org, loc
        :param entity_locator: The locator of the entity.
        :param tab_locator: The tab locator to switch to the entity's tab.
        :return: Returns whether the element is checked/selected or not.
        :rtype: bool
        :raises robottelo.ui.base.UINoSuchElementError: If the entity is not
            found via search.

        """
        go_to_page()
        searched = self.search_entity(entity_name, entity_locator)
        if searched is None:
            raise UINoSuchElementError('Entity not found via search.')
        searched.click()
        self.click(tab_locator)
        strategy, value = common_locators['all_values']
        selected = self.find_element(
            (strategy, value % context)).is_selected()
        return selected

    def submit_and_validate(self, locator, validation=True):
        """
        Submit the page and validate.

        :param str locator: The locator used to submit the page.
        :param bool validation: Helps enable or disable validation. Needs to be
            set to False for the negative tests.

        """
        self.click(locator)
        if self.wait_until_element(locator) and validation:
            raise UIPageSubmitionFailed('Page submission failed.')

    def is_element_enabled(self, locator):
        """Check whether UI element is enabled or disabled

        :param locator: The locator of the element.
        :return: Returns True if element is enabled and False otherwise

        """
        element = self.wait_until_element(locator)
        if element is None:
            return False
        self.wait_for_ajax()
        return element.is_enabled()

    def is_element_visible(self, locator):
        """Check whether UI element is visible

        :param locator: The locator of the element.
        :return: Returns True if element is visible and False otherwise

        """
        element = self.wait_until_element_exists(locator)
        if element is None:
            return False
        self.wait_for_ajax()
        return element.is_displayed()

    def click(self, locator, wait_for_ajax=True, timeout=30):
        """Locate the element described by the ``locator`` and click on it.

        :param locator: The locator that decribes the element.
        :param wait_for_ajax: Flag that indicates if should wait for AJAX after
            clicking on the element
        :param timeout: The amount of time that wait_fox_ajax should wait. This
            will have effect if ``wait_fox_ajax`` parameter is ``True``.
        :raise: UINoSuchElementError if the element could not be found.

        """
        element = self.wait_until_element(locator)
        if element is None:
            raise UINoSuchElementError(
                '{}: element with locator {} not found while trying to click.'
                .format(type(self).__name__, locator)
            )
        element.click()
        if wait_for_ajax:
            self.wait_for_ajax(timeout)
