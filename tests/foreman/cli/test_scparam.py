# -*- encoding: utf-8 -*-
# vim: ts=4 sw=4 expandtab ai
"""Test class for Smart Class Parameter CLI."""

from robottelo.cli.smartclass import SmartClassParameter
from robottelo.common.decorators import run_only_on
from robottelo.common import ssh
from robottelo.test import CLITestCase


@run_only_on('sat')
class TestSmartClassParameter(CLITestCase):
    """Test class for Smart Class Parameter CLI."""

    def run_puppet_module(self):
        """Import some parameterized puppet class. This is required to make sure
        that we have smart class variable available.

        """

        ssh.command('puppet module install --force puppetlabs/ntp')

    def test_bugzilla_1047794(self):
        """@Test: Check if SmartClass Paramter Info generates an error

        @Feature: SmartClass Paramter - Info

        @Assert: SmartClass Paramter Info does not generate an error

        """

        self.run_puppet_module()
        result = SmartClassParameter().list()
        self.assertEqual(
            result.return_code, 0, "Command should have succeeded")
        self.assertEqual(
            len(result.stderr), 0, "Should not have raised an error")
