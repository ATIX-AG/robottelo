"""Unit tests for sync plans."""
from datetime import datetime, timedelta
from ddt import ddt
from fauxfactory import gen_string
from nailgun import client, entities
from robottelo.common.helpers import get_server_credentials, get_server_url
from robottelo.common.decorators import (
    data,
    run_only_on,
    skip_if_bug_open,
    stubbed,
)
from robottelo.test import APITestCase


class SyncPlanTestCase(APITestCase):
    """Miscellaneous tests for sync plans."""

    def test_get_routes(self):
        """@Test: Issue an HTTP GET response to both available routes.

        @Assert: The same response is returned.

        @Feature: SyncPlan

        Targets BZ 1132817.

        """
        org = entities.Organization().create()
        entities.SyncPlan(organization=org).create()
        response1 = client.get(
            '{0}/katello/api/v2/sync_plans'.format(get_server_url()),
            auth=get_server_credentials(),
            data={'organization_id': org.id},
            verify=False,
        )
        response2 = client.get(
            '{0}/katello/api/v2/organizations/{1}/sync_plans'.format(
                get_server_url(),
                org.id
            ),
            auth=get_server_credentials(),
            verify=False,
        )
        for response in (response1, response2):
            response.raise_for_status()
        self.assertEqual(
            response1.json()['results'],
            response2.json()['results'],
        )


@stubbed()
@ddt
class SyncPlanCreateTestCase(APITestCase):
    """Tests specific to creating new sync plans."""

    @classmethod
    def setUpClass(cls):
        """Create an organization which can be re-used in tests."""
        cls.org = entities.Organization().create()
        super(SyncPlanCreateTestCase, cls).setUpClass()

    @stubbed()
    @run_only_on('sat')
    def test_create_disabled_sync_plan(self):
        """@Test: Create a disabled sync plan.

        @Assert: A disabled sync plan is created.

        @Feature: SyncPlan

        """

    @stubbed()
    @run_only_on('sat')
    @data(
        gen_string('alpha', 15),
        gen_string('alphanumeric', 15),
        gen_string('numeric', 15),
        gen_string('latin1', 15),
        gen_string('utf8', 15),
        gen_string('html', 15),
    )
    def test_create_sync_plan_with_random_name(self, name):
        """@Test: Create a sync plan with a random name.

        @Assert: A sync plan is created with the specified name.

        @Feature: SyncPlan

        """

    @stubbed()
    @run_only_on('sat')
    @data(
        gen_string('alpha', 15),
        gen_string('alphanumeric', 15),
        gen_string('numeric', 15),
        gen_string('latin1', 15),
        gen_string('utf8', 15),
        gen_string('html', 15),
    )
    def test_create_sync_plan_with_random_description(self, description):
        """@Test: Create a sync plan with a random description.

        @Assert: A sync plan is created with the specified description.

        @Feature: SyncPlan

        """

    @stubbed()
    @run_only_on('sat')
    @data(
        u'hourly',
        u'daily',
        u'weekly',
    )
    def test_create_sync_plan_with_random_interval(self, interval):
        """@Test: Create a sync plan with a random interval.

        @Assert: A sync plan is created with the specified interval.

        @Feature: SyncPlan

        """

    @stubbed()
    @run_only_on('sat')
    @data(
        # Today
        datetime.now(),
        # 5 minutes from now
        datetime.now() + timedelta(seconds=300),
        # 5 days from now
        datetime.now() + timedelta(days=5),
        # Yesterday
        datetime.now() - timedelta(days=1),
        # 5 minutes ago
        datetime.now() - timedelta(seconds=300),
    )
    def test_create_sync_plan_with_random_sync_date(self, syncdate):
        """@Test: Create a sync plan and update its sync date.

        @Assert: A sync plan can be created with a random sync date.

        @Feature: SyncPlan

        """

    @stubbed()
    @run_only_on('sat')
    @data(
        gen_string('alpha', 300),
        gen_string('alphanumeric', 300),
        gen_string('numeric', 300),
        gen_string('latin1', 300),
        gen_string('utf8', 300),
        gen_string('html', 300),
    )
    def test_create_sync_plan_with_invalid_random_name(self, name):
        """@Test: Create a sync plan with an invalid name.

        @Assert: A sync plan can not be created with the specified name.

        @Feature: SyncPlan

        """


@stubbed()
@ddt
class SyncPlanUpdateTestCase(APITestCase):
    """Tests specific to updating a sync plan."""

    @classmethod
    def setUpClass(cls):
        """Create an organization which can be re-used in tests."""
        cls.org = entities.Organization().create()
        super(SyncPlanUpdateTestCase, cls).setUpClass()

    @stubbed()
    @run_only_on('sat')
    def test_update_enabled_sync_plan(self):
        """@Test: Create a enabled sync plan then disable it.

        @Assert: An enabled sync plan is created and updated to be disabled.

        @Feature: SyncPlan

        """

    @stubbed()
    @run_only_on('sat')
    def test_update_disabled_sync_plan(self):
        """@Test: Create a disabled sync plan then enable it.

        @Assert: A disabled sync plan is created and updated to be enabled.

        @Feature: SyncPlan

        """

    @stubbed()
    @run_only_on('sat')
    @data(
        gen_string('alpha', 15),
        gen_string('alphanumeric', 15),
        gen_string('numeric', 15),
        gen_string('latin1', 15),
        gen_string('utf8', 15),
        gen_string('html', 15),
    )
    def test_update_sync_plan_with_random_name(self, name):
        """@Test: Create a sync plan and update its name.

        @Assert: A sync plan is created and its name can be updated with the
        specified name.

        @Feature: SyncPlan

        """

    @stubbed()
    @run_only_on('sat')
    @data(
        gen_string('alpha', 15),
        gen_string('alphanumeric', 15),
        gen_string('numeric', 15),
        gen_string('latin1', 15),
        gen_string('utf8', 15),
        gen_string('html', 15),
    )
    def test_update_sync_plan_with_random_description(self, description):
        """@Test: Create a sync plan and update its description.

        @Assert: A sync plan is created and its description can be updated with
        the specified description.

        @Feature: SyncPlan

        """

    @stubbed()
    @run_only_on('sat')
    @data(
        u'hourly',
        u'daily',
        u'weekly',
    )
    def test_update_sync_plan_with_random_interval(self, interval):
        """@Test: Create a sync plan and update its interval.

        @Assert: A sync plan is created and its interval can be updated with
        the specified interval.

        @Feature: SyncPlan

        """

    @stubbed()
    @run_only_on('sat')
    @data(
        # Today
        datetime.now(),
        # 5 minutes from now
        datetime.now() + timedelta(seconds=300),
        # 5 days from now
        datetime.now() + timedelta(days=5),
        # Yesterday
        datetime.now() - timedelta(days=1),
        # 5 minutes ago
        datetime.now() - timedelta(seconds=300),
    )
    def test_update_sync_plan_with_random_sync_date(self, syncdate):
        """@Test: Create a sync plan and update its sync date.

        @Assert: A sync plan can be created and its sync date can be updated
        with the specified sync date.

        @Feature: SyncPlan

        """


class SyncPlanProductTestCase(APITestCase):
    """Tests specific to adding/removing products to sync plans."""

    @classmethod
    def setUpClass(cls):
        """Create an organization and products which can be re-used in
        tests.

        """
        cls.org = entities.Organization().create()
        super(SyncPlanProductTestCase, cls).setUpClass()

    @run_only_on('sat')
    def test_add_product(self):
        """@Test: Create a sync plan and add one product to it.

        @Assert: A sync plan can be created and one product can be added to it.

        @Feature: SyncPlan

        """
        syncplan = entities.SyncPlan(organization=self.org).create()
        product = entities.Product(organization=self.org).create()
        syncplan.add_products([product.id])
        syncplan = syncplan.read()
        self.assertEqual(len(syncplan.product), 1)
        self.assertEqual(syncplan.product[0].id, product.id)

    @run_only_on('sat')
    def test_add_products(self):
        """@Test: Create a sync plan and add two products to it.

        @Assert: A sync plan can be created and two products can be added to
        it.

        @Feature: SyncPlan

        """
        syncplan = entities.SyncPlan(organization=self.org).create()
        products = [
            entities.Product(organization=self.org).create() for _ in range(2)
        ]
        syncplan.add_products([product.id for product in products])
        syncplan = syncplan.read()
        self.assertEqual(len(syncplan.product), 2)
        self.assertEqual(
            set((product.id for product in products)),
            set((product.id for product in syncplan.product)),
        )

    @skip_if_bug_open('bugzilla', 1199150)
    @run_only_on('sat')
    def test_remove_product(self):
        """@Test: Create a sync plan with two products and then remove one
        product from it.

        @Assert: A sync plan can be created and one product can be removed from
        it.

        @Feature: SyncPlan

        """
        syncplan = entities.SyncPlan(organization=self.org).create()
        products = [
            entities.Product(organization=self.org).create() for _ in range(2)
        ]
        syncplan.add_products([product.id for product in products])
        self.assertEqual(len(syncplan.read().product), 2)
        syncplan.remove_products([products[0].id])
        syncplan = syncplan.read()
        self.assertEqual(len(syncplan.product), 1)
        self.assertEqual(syncplan.product[0].id, products[1].id)

    @run_only_on('sat')
    def test_remove_products(self):
        """@Test: Create a sync plan with two products and then remove both
        products from it.

        @Assert: A sync plan can be created and both products can be removed
        from it.

        @Feature: SyncPlan

        """
        syncplan = entities.SyncPlan(organization=self.org).create()
        products = [
            entities.Product(organization=self.org).create() for _ in range(2)
        ]
        syncplan.add_products([product.id for product in products])
        self.assertEqual(len(syncplan.read().product), 2)
        syncplan.remove_products([product.id for product in products])
        self.assertEqual(len(syncplan.read().product), 0)

    @skip_if_bug_open('bugzilla', 1199150)
    @run_only_on('sat')
    def test_repeatedly_add_remove(self):
        """@Test: Repeatedly add and remove a product from a sync plan.

        @Assert: A task is returned which can be used to monitor the additions
        and removals.

        @Feature: SyncPlan

        """
        syncplan = entities.SyncPlan(organization=self.org).create()
        product = entities.Product(organization=self.org).create()
        for _ in range(5):
            syncplan.add_products([product.id])
            self.assertEqual(len(syncplan.read().product), 1)
            syncplan.remove_products([product.id])
            self.assertEqual(len(syncplan.read().product), 0)


@stubbed()
class SyncPlanSynchronizeTestCase(APITestCase):
    """Tests specific to synchronizing sync plans."""

    @classmethod
    def setUpClass(cls):
        """Create an organization and products which can be re-used in
        tests."""
        cls.org = entities.Organization().create()
        cls.products = [
            entities.Product(organization=cls.org).create() for _ in range(2)
        ]
        super(SyncPlanSynchronizeTestCase, cls).setUpClass()

    @stubbed()
    @run_only_on('sat')
    def test_synchronize_sync_plan_with_one_product(self):
        """@Test: Create a sync plan with one product and sync it.

        @Assert: A sync plan is created with one product and product can be
        synchronized.

        @Feature: SyncPlan

        """

    @stubbed()
    @run_only_on('sat')
    def test_synchronize_sync_plan_with_two_products(self):
        """@Test: Create a sync plan with two products and sync them.

        @Assert: A sync plan is created with one product and products can be
        synchronized.

        @Feature: SyncPlan

        """


@stubbed()
class SyncPlanDeleteTestCase(APITestCase):
    """Tests specific to deleting sync plans."""

    @classmethod
    def setUpClass(cls):
        """Create an organization which can be re-used in tests."""
        cls.org = entities.Organization().create()
        super(SyncPlanDeleteTestCase, cls).setUpClass()

    @stubbed()
    @run_only_on('sat')
    def test_delete_sync_plan_with_one_product(self):
        """@Test: Create a sync plan with one product and delete it.

        @Assert: A sync plan is created with one product and sync plan can be
        deleted.

        @Feature: SyncPlan

        """

    @stubbed()
    @run_only_on('sat')
    def test_delete_sync_plan_with_two_products(self):
        """@Test: Create a sync plan with two products and delete them.

        @Assert: A sync plan is created with one product and sync plan can be
        deleted.

        @Feature: SyncPlan

        """

    @stubbed()
    @run_only_on('sat')
    def test_delete_sync_plan_with_one_synced_product(self):
        """@Test: Create a sync plan with one synced product and delete it.

        @Assert: A sync plan is created with one synced product and sync plan
        can be deleted.

        @Feature: SyncPlan

        """
