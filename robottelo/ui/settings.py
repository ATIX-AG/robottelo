# -*- encoding: utf-8 -*-
"""
Implements Settings UI
"""

from robottelo.ui.base import Base, UINoSuchElementError
from robottelo.ui.locators import locators
from selenium.webdriver.support.select import Select


class OptionError(ValueError):
    """Indicates that value_type is other than 'input' and 'dropdown'"""


class Settings(Base):
    """
    Implements the Update function to edit/update settings
    """

    def search(self, name):
        """
        Searches existing parameter from UI
        """
        element = self.search_entity(name, locators["settings.param"])
        return element

    def update(self, tab_locator, param_name, value_type, param_value):
        """
        Updates the value of selected parameter under settings

        @param tab_locator: Selenium locator to select appropriate tab.
        @param param_name: A valid parameter name.
        @param value_type: Valid value type either 'input' or 'dropdown'
        @param param_value: Value of selected parameter

        @raise OptionError: Raise an exception when value type is different
        than 'input' and 'dropdown'.
        @raise UINoSuchElementError: Raise an exception when UI element is
        not found
        """

        if self.wait_until_element(tab_locator):
            self.find_element(tab_locator).click()
            strategy, value = locators["settings.edit_param"]
            element = self.wait_until_element((strategy,
                                               value % param_name))
            if element:
                element.click()
                if value_type == "dropdown":
                    Select(self.find_element
                           (locators["settings.select_value"])
                           ).select_by_value(param_value)
                elif value_type == "input":
                    self.field_update("settings.input_value", param_value)
                else:
                    raise OptionError(
                        "Please input appropriate value type")
                self.wait_for_ajax()
                self.wait_until_element(locators["settings.save"]).click()
                self.wait_for_ajax()
            else:
                raise UINoSuchElementError(
                    "Couldn't find edit button to update selected param")
        else:
            raise UINoSuchElementError(
                "Couldn't find the tab with name: '%s'" % tab_locator)

    def get_saved_value(self, tab_locator, param_name):
        """
        Fetch the updated value to assert
        """

        if self.wait_until_element(tab_locator):
            self.find_element(tab_locator).click()
            strategy, value = locators["settings.edit_param"]
            element = self.wait_until_element((strategy,
                                               value % param_name))
            if element:
                return element.text
            else:
                raise UINoSuchElementError(
                    "Couldn't find element to fetch the param's value")
