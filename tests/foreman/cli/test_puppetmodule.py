# -*- encoding: utf-8 -*-
# vim: ts=4 sw=4 expandtab ai

# pylint: disable=R0904
"""Test class for PuppetModule CLI"""

from robottelo.test import CLITestCase
from robottelo.cli.puppetmodule import PuppetModule
from robottelo.common.decorators import skip_if_bug_open


class TestPuppetModule(CLITestCase):
    """Tests for PuppetModule via Hammer CLI"""

    @skip_if_bug_open('bugzilla', 1127382)
    def test_bugzilla_1127382(self):
        """@Test: hammer puppet-module <info,list> --help

        @Feature: puppet-module info/list

        @Assert: Assert product option are present

        """
        # puppet-module list --help:
        result = PuppetModule.list({'help': True})
        # get list of lines and check they all are unique
        lines = [line['message'] for line in result.stdout]
        self.assertEqual(len(set(lines)), len(lines),
                         'The help should not have repeat options')
        product_options = [line for line in lines
                           if line.startswith('--product')]
        self.assertGreater(len(product_options), 0,
                           'At least one --product option should be present')

        # puppet-module info --help:info, ignore exception
        result = PuppetModule.info({'help': True})
        # get list of lines and check they all are unique
        lines = [line for line in result.stdout['options']]
        self.assertEqual(len(set(lines)), len(lines),
                         'The help should not have repeat options')
        product_options = [line for line in lines
                           if line.startswith('--product')]
        self.assertGreater(len(product_options), 0,
                           'At least one --product option should be present')
