# -*- encoding: utf-8 -*-
# vim: ts=4 sw=4 expandtab ai
"""Test class for Reports CLI."""

import random

from robottelo.cli.report import Report
from robottelo.common import ssh
from robottelo.test import CLITestCase


class TestReport(CLITestCase):
    """Test class for Reports CLI. """

    def setUp(self):
        super(TestReport, self).setUp()
        self.run_puppet_agent()

    def run_puppet_agent(self):
        """Retrieves the client configuration from the puppet master and
        applies it to the local host. This is required to make sure
        that we have reports available.

        """

        ssh.command('puppet agent -t')

    def test_list(self):
        """@Test: Test list for Puppet report

        @Feature: Puppet Report - list

        @Assert: Puppert Report List is displayed

        """

        result = Report.list()
        self.assertEqual(result.return_code, 0)
        self.assertGreater(len(result.stdout), 0)

    def test_info(self):
        """@Test: Test Info for Puppet report

        @Feature: Puppet Report - Info

        @Assert: Puppet Report Info is displayed

        """

        result = Report.list()
        self.assertEqual(result.return_code, 0)
        self.assertGreater(len(result.stdout), 0)

        # Grab a random report
        report = random.choice(result.stdout)
        result = Report.info({'id': report['id']})
        self.assertEqual(result.return_code, 0)
        self.assertEqual(report['id'], result.stdout['id'])

    def test_delete(self):
        """@Test: Check if Puppet Report can be deleted

        @Feature: Puppet Report - Delete

        @Assert: Puppet Report is deleted

        """

        result = Report.list()
        self.assertEqual(result.return_code, 0)
        self.assertGreater(len(result.stdout), 0)

        # Grab a random report
        report = random.choice(result.stdout)
        result = Report.delete({'id': report['id']})
        self.assertEqual(result.return_code, 0)

        result = Report.info({'id': report['id']})
        self.assertGreater(result.return_code, 0)
        self.assertGreater(len(result.stderr), 0)
