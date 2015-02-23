# -*- encoding: utf-8 -*-
"""Test class for Multi-Network Support feature"""
from robottelo.test import UITestCase
from robottelo.common.decorators import stubbed


class Multinetwork(UITestCase):
    """Implements Multi Network support tests in UI."""

    @stubbed()
    def test_create_host_1(self):
        """@Test: Create host with default interface and set 'DHCP' for IPAM
        and BootMode for provisioning subnet

        @Feature: Multi Network Support

        @Setup: Provisioning should be configured

        @Steps:

        1. Set 'DHCP' for IPAM and BootMode for provisioning subnet
        2. All other fields on subnet page should be filled

        @Assert: Host should be provisioned with correct configuration under
        /etc/sysconfig/network-scripts/ifcfg-<interface>

        @Status: Manual

        """

    @stubbed()
    def test_create_host_2(self):
        """@Test: Create host with default interface when IPAM set as
        'Internal DB' (without specifying start and end range) and BootMode
        set as 'DHCP' for provisioning subnet

        @Feature: Multi Network Support

        @Setup: Provisioning should be configured

        @Steps:

        1. Set IPAM with 'Internal DB' and BootMode with 'DHCP for provisioning
           subnet
        2. All other fields on subnet page should be filled except start and
           end IP range

        @Assert: Host should be provisioned with correct configuration under
        /etc/sysconfig/network-scripts/ifcfg-<interface>

        @Status: Manual

        """

    @stubbed()
    def test_create_host_3(self):
        """@Test: Create host with default interface when IPAM set as
        'Internal DB' (with start and end IP range) and BootMode set as
        'DHCP' for provisioning subnet

        @Feature: Multi Network Support

        @Setup: Provisioning should be configured

        @Steps:

        1. Set IPAM with 'Internal DB' and BootMode with 'DHCP for provisioning
           subnet
        2. All other fields on subnet page should be filled including start and
           end IP range

        @Assert: Host should be provisioned with correct configuration under
        /etc/sysconfig/network-scripts/ifcfg-<interface>

        @Status: Manual

        """

    @stubbed()
    def test_create_host_4(self):
        """@Test: Create host with default interface when IPAM set as
        'Internal DB' (with start and end IP range) and BootMode set as
        'Static' for provisioning subnet

        @Feature: Multi Network Support

        @Setup: Provisioning should be configured

        @Steps:

        1. Set IPAM with 'Internal DB' and BootMode with 'Static' for
           provisioning subnet
        2. All other fields on subnet page should be filled including start and
           end IP range

        @Assert: Host should be provisioned with correct configuration under
        /etc/sysconfig/network-scripts/ifcfg-<interface>

        @Status: Manual

        """

    @stubbed()
    def test_create_host_5(self):
        """@Test: Create host with default interface when IPAM set as
        'Internal DB' (without start and end IP range) and BootMode set
        as 'Static' for provisioning subnet

        @Feature: Multi Network Support

        @Setup: Provisioning should be configured

        @Steps:

        1. Set IPAM with 'Internal DB' and BootMode with 'Static' for
           provisioning subnet
        2. All other fields on subnet page should be filled except start and
           end IP range

        @Assert: Host should be provisioned with correct configuration under
        /etc/sysconfig/network-scripts/ifcfg-<interface>

        @Status: Manual

        """

    @stubbed()
    def test_create_host_6(self):
        """@Test: Create host with default interface when IPAM set as 'DHCP'
        (with start and end IP range) and BootMode set as 'Static' for
        provisioning subnet

        @Feature: Multi Network Support

        @Setup: Provisioning should be configured

        @Steps:

        1. Set IPAM with 'DHCP' and BootMode with 'Static' for provisioning
           subnet
        2. All other fields on subnet page should be filled including start and
           end IP range

        @Assert: Host should be provisioned with correct configuration under
        /etc/sysconfig/network-scripts/ifcfg-<interface>

        @Status: Manual

        """

    @stubbed()
    def test_create_host_7(self):
        """@Test: Create host with default interface when IPAM set as 'DHCP'
        (without start and end IP range) and BootMode set as 'Static' for
        provisioning subnet

        @Feature: Multi Network Support

        @Setup: Provisioning should be configured

        @Steps:

        1. Set IPAM with 'DHCP' and BootMode with 'Static' for provisioning
           subnet
        2. All other fields on subnet page should be filled except start and
           end IP range

        @Assert: Host should be provisioned with correct configuration under
        /etc/sysconfig/network-scripts/ifcfg-<interface>

        @Status: Manual

        """

    @stubbed()
    def test_create_host_8(self):
        """@Test: Create host with default interface when IPAM set as 'None'
        and BootMode set as 'Static' for provisioning subnet

        @Feature: Multi Network Support

        @Setup: Provisioning should be configured

        @Steps:

        1. Set IPAM with 'None' and BootMode with 'Static' for provisioning
           subnet
        2. All other fields on subnet page should be filled

        @Assert: Host should be provisioned with correct configuration under
        /etc/sysconfig/network-scripts/ifcfg-<interface>

        @Status: Manual

        """

    @stubbed()
    def test_create_host_9(self):
        """@Test: Create host with default interface when IPAM set as 'None'
        and BootMode set as 'DHCP' for provisioning subnet

        @Feature: Multi Network Support

        @Setup: Provisioning should be configured

        @Steps:

        1. Set IPAM with 'None' and BootMode with 'DHCP' for provisioning
           subnet
        2. All other fields on subnet page should be filled

        @Assert: Host should be provisioned with correct configuration under
        /etc/sysconfig/network-scripts/ifcfg-<interface>

        @Status: Manual

        """

    @stubbed()
    def test_add_alias_interface_1(self):
        """@Test:  Add an alias interface(eth0:0) with mac different than
        primary interface's mac

        @Feature: Multi Network Support

        @Setup: Provisioning should be configured

        @Steps:

        1. Go to 'Network' tab of 'New host' page
        2. Click on 'Add Interface' from 'Network tab
        3. Choose Type: 'Interface'
        4. mac address: should be different from primary interface
        5. Identifier: eth0:0
        6. Select 'Managed'
        7. Select 'Virtual Nic'
        8. attached_to: identifier of primary interface(eth0)
        9. Fill all other details correctly in new host form and submit it

        @Assert: Validation error should be raised as mac address of alias
        interface should be same as of primary interface

        @Status: Manual

        """

    @stubbed()
    def test_add_alias_interface_2(self):
        """@Test:  Add an alias interface(eth0:0) without selecting virtual nic

        @Feature: Multi Network Support

        @Setup: Provisioning should be configured

        @Steps:

        1. Go to 'Network' tab of 'New host' page
        2. Click on 'Add Interface' from 'Network tab
        3. Choose Type: 'Interface'
        4. mac address: mac should be same as of primary interface
        5. Identifier: eth0:0
        6. Select 'Managed'
        7. Fill all other details correctly in new host form and submit it

        @Assert: Validation error should be raised as two nics can not have
        same mac

        @Status: Manual

        """

    @stubbed()
    def test_add_alias_interface_3(self):
        """@Test:  Add an alias interface(eth0:0) without defining
        'attached_to' interface under 'Virtual Nic'

        @Feature: Multi Network Support

        @Setup: Provisioning should be configured

        @Steps:

        1. Go to 'Network' tab of 'New host' page
        2. Click on 'Add Interface' from 'Network tab
        3. Choose Type: 'Interface'
        4. mac address: mac should be same as of primary interface
        5. Identifier: eth0:0
        6. Select 'Managed'
        7. Select 'Virtual Nic'
        8. Do not specify anything under 'attached_to'
        9. Fill all other details correctly in new host form and submit it

        @Assert: Validation error should be raised as attached_to is mandatory
        option to create alias interface

        @Status: Manual

        """

    @stubbed()
    def test_add_alias_interface_4(self):
        """@Test:  Add an alias interface(eth0:0) when bootMode set to 'DHCP'
        mode under selected subnet

        @Feature: Multi Network Support

        @Setup: Provisioning should be configured

        @Steps:

        1. Go to 'Network' tab of 'New host' page
        2. Click on 'Add Interface' from 'Network tab
        3. Choose Type: 'Interface'
        4. mac address: mac should be same as of primary interface
        5. Identifier: eth0:0
        6. Select 'Managed'
        7. Select 'Virtual Nic'
        8. attached_to: identifier of primary interface(eth0)
        9. Go to Infrastructure → Subnet
        10. Set IPAM mode to 'Internal DB'
        11. BootMode 'DHCP'
        12. Fill all other details correctly in new host form and submit it

        @Assert: Validation error should be raised as you can't configure alias
        interface in 'DHCP' mode.

        @Status: Manual

        """

    @stubbed()
    def test_add_alias_interface_5(self):
        """@Test:  Add an alias interface(eth0:0) when bootMode set to 'Static'
        mode under selected subnet

        @Feature: Multi Network Support

        @Setup: Provisioning should be configured

        @Steps:

        1. Go to 'Network' tab of 'New host' page
        2. Click on 'Add Interface' from 'Network tab
        3. Choose Type: 'Interface'
        4. mac address: mac should be same as of primary interface
        5. Identifier: eth0:0
        5. Select 'Managed'
        6. Select 'Virtual Nic'
        7. attached_to: identifier of primary interface(eth0)
        8. Go to Infrastructure → Subnet
        9. Set IPAM mode to 'Internal DB'
        10. BootMode 'Static'
        11. Fill all other details correctly in new host form and submit it

        @Assert: Interface should be configured successfully and correct
        configuration should displayed on proviisoned host
        under /etc/sysconfig/network-scripts/ifcfg-<interface_name>

        @Status: Manual

        """

    @stubbed()
    def test_add_alias_interface_6(self):
        """@Test:  Add an interface with same identifier of exiting interface
        Like interfaces eth0, eth0:0 already exists and now create new
        interface with eth0:0 identifier

        @Feature: Multi Network Support

        @Setup: Provisioning should be configured

        @Steps:

        1. Go to 'Network' tab of 'New host' page
        2. Click on 'Add Interface' from 'Network tab
        3. Choose Type: 'Interface'
        4. mac address: mac should be same as of primary interface
        5. Identifier: eth0:0
        6. Select 'Managed'
        7. Select 'Virtual Nic'
        8. attached_to: identifier of primary interface(eth0)
        9. Go to Infrastructure → Subnet
        10. Set IPAM mode to 'Internal DB'
        11. BootMode 'Static'
        12. Fill all other details correctly in new host form and submit it

        @Assert: Validation error should be raised on UI

        @Status: Manual

        """

    @stubbed()
    def test_delete_alias_interface(self):
        """@Test:  Delete an alias interface

        @Feature: Multi Network Support

        @Setup: Provisioning should be configured

        @Steps:

        1. Create an aliased interface
        2. Edit the new host → Network → delete the selected interface
        3. submit form

        @Assert: Interface should be deleted successfully

        @Status: Manual

        """

    @stubbed()
    def test_add_bond_interface_1(self):
        """@Test: Add bond interface using existing two interfaces

        @Feature: Multi Network Support

        @Setup: Provisioning should be configured

        @Steps:

        1. Go to 'Network' tab of 'New host' page
        2. Click on 'Add Interface' from 'Network tab
        3. Choose Type: 'Bond'
        4. mac address: mac should be same as of any of two primary interfaces
        5. Identifier: bond0
        6. Select 'Managed'
        7. Mode 'Balanced rr'
        8. attached_devices: eth0, eth1
        9. Go to Infrastructure → Subnet
        10. Set IPAM mode to 'Internal DB'
        11. BootMode 'Static'
        12. Fill all other details correctly in new host form and submit it

        @Assert: Interface should be configured successfully with name bond0

        @Status: Manual

        """

    @stubbed()
    def test_add_bond_interface_2(self):
        """@Test: Add bond interface using existing two interfaces without
        specifying mac

        @Feature: Multi Network Support

        @Setup: Provisioning should be configured

        @Steps:

        1. Go to 'Network' tab of 'New host' page
        2. Click on 'Add Interface' from 'Network tab
        3. Choose Type: 'Bond'
        4. mac address: leave it blank
        5. Identifier: bond0
        6. Select 'Managed'
        7. Mode 'Balanced rr'
        8. attached_devices: eth0, eth1
        9. Go to Infrastructure → Subnet
        10. Set IPAM mode to 'Internal DB'
        11. BootMode 'Static'
        12. Fill all other details correctly in new host form and submit it

        @Assert: UI should raise validation error as user shouldn't be allowed
        create bond interface without mac

        @Status: Manual

        """

    @stubbed()
    def test_add_bond_interface_3(self):
        """@Test: Add bond interface without specifying attached devices

        @Feature: Multi Network Support

        @Setup: Provisioning should be configured

        @Steps:

        1. Go to 'Network' tab of 'New host' page
        2. Click on 'Add Interface' from 'Network tab
        3. Choose Type: 'Bond'
        4. mac address: leave it blank
        5. Identifier: bond0
        6. Select 'Managed'
        7. Mode 'Balanced rr'
        8. attached_devices: leave it blank
        9. Go to Infrastructure → Subnet
        10. Set IPAM mode to 'Internal DB'
        11. BootMode 'Static'
        12. Fill all other details correctly in new host form and submit it

        @Assert: Interface should be configured successfully without attaching
        any device to it.

        @Status: Manual

        """

    @stubbed()
    def test_add_bond_interface_4(self):
        """@Test: Add bond interface with one alias interface

        @Feature: Multi Network Support

        @Setup: Provisioning should be configured

        @Steps:

        1. Alias interface should already be configured
        2. Go to 'Network' tab of 'New host' page
        3. Click on 'Add Interface' from 'Network tab
        4. Choose Type: 'Bond'
        5. mac address: leave it blank
        6. Identifier: bond0
        7. Select 'Managed'
        8. Mode 'Balanced rr'
        9. attached_devices: eth0, eth0:0
        10. Go to Infrastructure → Subnet
        11. Set IPAM mode to 'Internal DB'
        12. BootMode 'Static'
        13. Fill all other details correctly in new host form and submit it

        @Assert: Interface should be configured successfully with name bond0
        attached to eth0 eth0:0

        @Status: Manual

        """

    @stubbed()
    def test_add_bmc_interface_1(self):
        """@Test: Add bmc interface

        @Feature: Multi Network Support

        @Setup: Provisioning should be configured

        @Steps:

        1. Go to 'Network' tab of 'New host' page
        2. Click on 'Add Interface' from 'Network tab
        3. Choose Type: 'BMC'
        4. mac address: Mac of BMC
        5. Identifier: bmc
        6. Select 'Managed'
        7. User name:
        8. password:
        9. Provider: IPMI
        10. Fill all other details correctly in new host form and submit it

        @Assert: Interface should be configured successfully and user
        should get On/OFF button on host page

        @Status: Manual

        """

    @stubbed()
    def test_add_bmc_interface_2(self):
        """@Test: Add bmc interface without mac

        @Feature: Multi Network Support

        @Setup: Provisioning should be configured

        @Steps:

        1. Go to 'Network' tab of 'New host' page
        2. Click on 'Add Interface' from 'Network tab
        3. Choose Type: 'BMC'
        4. mac address: blank
        5. Identifier: bmc
        6. Select 'Managed'
        7. User name:
        8. password:
        9. Provider: IPMI
        10. Fill all other details correctly in new host form and submit it

        @Assert: UI should raise validation error

        @Status: Manual

        """
