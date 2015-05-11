"""Test class for Puppet Classes UI"""

from ddt import ddt
from fauxfactory import gen_string
from nailgun import entities
from robottelo.common.decorators import (
    data, run_only_on, skip_if_bug_open)
from robottelo.common.helpers import generate_strings_list
from robottelo.test import UITestCase
from robottelo.ui.session import Session


@run_only_on('sat')
@ddt
class PuppetClasses(UITestCase):
    """Implements puppet classes tests in UI."""

    @data({'description': gen_string('alpha', 255)},
          {'description': gen_string('numeric', 255)},
          {'description': gen_string('alphanumeric', 255)},
          {'description': gen_string('utf8', 10)},
          {'description': gen_string('latin1', 10)})
    def test_update_positive_1(self, testdata):
        """@Test: Create new puppet-class

        @Feature: Puppet-Classes - Positive Update

        @Assert: Puppet-Classes is updated.

        """
        class_name = 'foreman_scap_client'
        param_name = 'ca file'
        description = testdata['description']
        with Session(self.browser):
            # Importing puppet classes from puppet-foreman_scap_client
            # module for update process
            if self.puppetclasses.search(class_name) is None:
                self.puppetclasses.import_scap_client_puppet_classes()
            self.assertIsNotNone(self.puppetclasses.search(class_name))
            self.puppetclasses.update_class_parameter_description(
                class_name,
                param_name,
                description
            )
            self.assertEqual(
                description,
                self.puppetclasses.fetch_class_parameter_description(
                    class_name,
                    param_name)
            )

    @skip_if_bug_open('bugzilla', 1126473)
    @data(*generate_strings_list(len1=8))
    def test_delete_positive_1(self, name):
        """@Test: Create new puppet-class

        @Feature: Puppet-Classes - Positive delete

        @Assert: Puppet-Class is deleted

        @BZ: 1126473

        """
        entities.PuppetClass(name=name).create_json()
        with Session(self.browser):
            self.assertIsNotNone(self.puppetclasses.search(name))
            self.puppetclasses.delete(name, True)
            self.assertIsNone(self.puppetclasses.search(name))
