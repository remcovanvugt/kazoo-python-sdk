#!/usr/bin/env python
import kazoo
import unittest
import pprint
import random


class FunctionalTest(unittest.TestCase):
    def auth(self, username=None, password=None, account_name=None, base_url=None):

        if username is not None:
            self.username = username
        else:
            self.username = ''

        if password is not None:
            self.password = password
        else:
            self.password = ''

        if account_name is not None:
            self.account_name = account_name
        else:
            self.account_name = ''

        if base_url is not None:
            self.base_url = base_url
        else:
            self.base_url = ''

        client = kazoo.Client(username=self.username, password=self.password, account_name=self.account_name,
                              base_url=self.base_url)
        client.authenticate()
        return client

    def testAuth(self):
        self.client = self.auth()
        self.assertGreater(len(self.client.account_id),0)

class DeviceTest(FunctionalTest):
    def setUp(cls):
        DeviceTest.client = FunctionalTest.auth()

    def test_0_CreateDevice(self):
        data={}
        DeviceTest.a_name = 'SDKTest'+str(random.randint(100,1000))
        data['name']= DeviceTest.a_name
        DeviceTest.a_device = DeviceTest.create_device(DeviceTest.client.account_id,data)
        self.assertGreater(len(DeviceTest.a_device['data']['id']),0)
'''''
    def test_1_FetchDevice(self):
        test_data = DeviceTest.client.get_device(DeviceTest.client.account_id,DeviceTest.a_device['data']['id'])
        self.assertEqual(DeviceTest.a_name, test_data['data']['name'])

    def test_2_UpdateDevice(self):
        DeviceTest.a_name = 'SDKTest'+str(random.randint(100,1000))
        data = {}
        data['name'] = DeviceTest.a_name
        DeviceTest.client.update_device(DeviceTest.client.account_id,DeviceTest.a_device['data']['id'], data)
        test_data = DeviceTest.client.get_device(DeviceTest.client.account_id, DeviceTest.a_device['data']['id'])
        self.assertEqual(DeviceTest.a_name, test_data['data']['name'])

    def test_3_DeviceListing(self):
        data = DeviceTest.client.get_devices(DeviceTest.client.account_id)
        self.assertEqual(len(data['data']), 1)

    def test_4_DeviceListingFilter(self):
        filter_data = {}
        filter_data['filter_name'] = DeviceTest.a_name
        test_data = DeviceTest.client.get_devices(DeviceTest.client.account_id, filter_data)
        self.assertEqual(len(test_data['data']), 1)

    def test_8_RemoveDevice(self):
        DeviceTest.client.delete_device(DeviceTest.client.account_id,DeviceTest.a_device['data']['id'])
        data = DeviceTest.client.get_devices(DeviceTest.client.account_id)
        self.assertEqual(len(data['data']), 0)
'''

class MenusTest(FunctionalTest):
    def setUp(self):
        MenusTest.client = FunctionalTest.auth(self)

    def test_0_CreateMenu(self):
        data={}
        MenusTest.a_name = 'SDKTest'+str(random.randint(100,1000))
        data['name']= MenusTest.a_name
        MenusTest.a_menu = MenusTest.client.create_menu(MenusTest.client.account_id,data)
        self.assertGreater(len(MenusTest.a_menu['data']['id']),0)

    def test_1_FetchDevice(self):
        test_data = MenusTest.client.get_menu(MenusTest.client.account_id,MenusTest.a_menu['data']['id'])
        self.assertEqual(MenusTest.a_name, test_data['data']['name'])

    def test_2_UpdateMenu(self):
        MenusTest.a_name = 'SDKTest'+str(random.randint(100,1000))
        data = {}
        data['name'] = MenusTest.a_name
        MenusTest.client.update_menu(MenusTest.client.account_id,MenusTest.a_menu['data']['id'], data)
        test_data = MenusTest.client.get_menu(MenusTest.client.account_id, MenusTest.a_menu['data']['id'])
        self.assertEqual(MenusTest.a_name, test_data['data']['name'])

    def test_3_MenuListing(self):
        data = MenusTest.client.get_menus(MenusTest.client.account_id)
        self.assertEqual(len(data['data']), 5) # Default Menu

    def test_4_MenuListingFilter(self):
        filter_data = {}
        filter_data['filter_name'] = MenusTest.a_name
        test_data = MenusTest.client.get_menus(MenusTest.client.account_id, filter_data)
        self.assertEqual(len(test_data['data']), 1)

    def test_8_RemoveMenu(self):
        MenusTest.client.delete_menu(MenusTest.client.account_id,MenusTest.a_menu['data']['id'])
        data = MenusTest.client.get_menus(MenusTest.client.account_id)
        self.assertEqual(len(data['data']), 4) # Default Menu


if __name__ == '__main__':
     unittest.main(verbosity=3)
