"""Test class for Subscriptions"""
from ddt import ddt
from robottelo.cli.factory import make_org
from robottelo.cli.repository import Repository
from robottelo.cli.repository_set import RepositorySet
from robottelo.cli.subscription import Subscription
from robottelo.common import manifests
from robottelo.common.decorators import skip_if_bug_open
from robottelo.common.ssh import upload_file
from robottelo.test import CLITestCase


@ddt
class TestSubscription(CLITestCase):
    """Manifest CLI tests"""

    def setUp(self):  # noqa
        """Tests for content-view via Hammer CLI"""
        super(TestSubscription, self).setUp()
        self.org = make_org()
        self.manifest = manifests.clone()

    def _upload_manifest(self, manifest, org_id):
        """Uploads a manifest file and import it into an organization"""
        upload_file(manifest, remote_file=manifest)
        result = Subscription.upload({
            'file': manifest,
            'organization-id': org_id,
        })
        self.assertEqual(result.return_code, 0)
        self.assertEqual(len(result.stderr), 0)

    def test_manifest_upload(self):
        """@Test: upload manifest (positive)

        @Feature: Subscriptions/Manifest Upload

        @Assert: Manifest are uploaded properly

        """
        self._upload_manifest(self.manifest, self.org['id'])
        result = Subscription.list(
            {'organization-id': self.org['id']},
            per_page=False)
        self.assertEqual(result.return_code, 0)
        self.assertEqual(len(result.stderr), 0)

    @skip_if_bug_open('bugzilla', 1207501)
    def test_manifest_delete(self):
        """@Test: Delete uploaded manifest (positive)

        @Feature: Subscriptions/Manifest Delete

        @Assert: Manifest are deleted properly

        @BZ: 1207501

        """
        self._upload_manifest(self.manifest, self.org['id'])
        result = Subscription.list(
            {'organization-id': self.org['id']},
            per_page=False
        )
        self.assertEqual(result.return_code, 0)
        self.assertEqual(len(result.stderr), 0)

        result = Subscription.delete_manifest({
            'organization-id': self.org['id'],
        })
        self.assertEqual(result.return_code, 0)
        self.assertEqual(len(result.stderr), 0)

        result = Subscription.list(
            {'organization-id': self.org['id']},
            per_page=False
        )
        self.assertEqual(result.return_code, 0)
        self.assertEqual(len(result.stdout), 0)

    def test_enable_manifest_repository_set(self):
        """@Test: enable repository set (positive)

        @Feature: Subscriptions/Repository Sets

        @Assert: you are able to enable and synchronize
        repository contained in a manifest

        """
        self._upload_manifest(self.manifest, self.org['id'])
        result = Subscription.list(
            {'organization-id': self.org['id']},
            per_page=False
        )
        self.assertEqual(result.return_code, 0)
        self.assertEqual(len(result.stderr), 0)

        result = RepositorySet.enable({
            'name': (
                'Red Hat Enterprise Virtualization Agents '
                'for RHEL 6 Workstation (RPMs)'
            ),
            'organization-id': self.org['id'],
            'product': 'Red Hat Enterprise Linux Workstation',
            'releasever': '6Workstation',
            'basearch': 'x86_64',
        })
        self.assertEqual(result.return_code, 0)
        self.assertEqual(len(result.stderr), 0)

        result = Repository.synchronize({
            'name': (
                'Red Hat Enterprise Virtualization Agents '
                'for RHEL 6 Workstation '
                'RPMs x86_64 6Workstation'
            ),
            'organization-id': self.org['id'],
            'product': 'Red Hat Enterprise Linux Workstation',
        })

        self.assertEqual(result.return_code, 0)
        self.assertEqual(len(result.stderr), 0)

    def test_manifest_history(self):
        """@Test: upload manifest (positive) and check history

        @Feature: Subscriptions/Manifest History

        @Assert: Manifest history is shown properly

        """
        self._upload_manifest(self.manifest, self.org['id'])
        result = Subscription.list(
            {'organization-id': self.org['id']},
            per_page=None
        )
        self.assertEqual(result.return_code, 0)
        self.assertEqual(len(result.stderr), 0)

        result = Subscription.manifest_history({
            'organization-id': self.org['id'],
        })
        self.assertEqual(result.return_code, 0)
        self.assertEqual(len(result.stderr), 0)
        self.assertIn(
            '{0} file imported successfully.'.format(self.org['name']),
            ''.join(result.stdout)
        )

    def test_manifest_refresh(self):
        """@Test: upload manifest (positive) and refresh

        @Feature: Subscriptions/Manifest refresh

        @Assert: Manifests can be refreshed

        """
        self._upload_manifest(
            manifests.download_manifest_template(), self.org['id'])
        result = Subscription.list(
            {'organization-id': self.org['id']},
            per_page=False
        )
        self.assertEqual(result.return_code, 0)
        self.assertEqual(len(result.stderr), 0)

        result = Subscription.refresh_manifest({
            'organization-id': self.org['id'],
        })
        self.assertEqual(result.return_code, 0)
        self.assertEqual(len(result.stderr), 0)

        result = Subscription.delete_manifest({
            'organization-id': self.org['id'],
        })
        self.assertEqual(result.return_code, 0)
        self.assertEqual(len(result.stderr), 0)

    @skip_if_bug_open('bugzilla', 1226425)
    def test_invalid_manifest_refresh(self):
        """@Test: manifest refresh must fail with a cloned manifest

        @Feature: Subscriptions/Manifest refresh

        @Assert: the refresh command returns a non-zero return code

        @BZ: 1226425

        """
        self._upload_manifest(self.manifest, self.org['id'])
        result = Subscription.list(
            {'organization-id': self.org['id']},
            per_page=False
        )
        self.assertEqual(result.return_code, 0)
        self.assertEqual(len(result.stderr), 0)

        result = Subscription.refresh_manifest({
            'organization-id': self.org['id'],
        })
        self.assertNotEqual(result.return_code, 0)
        self.assertNotEqual(len(result.stderr), 0)
