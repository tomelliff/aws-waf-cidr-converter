import unittest

import netaddr

import converter


class TestConvertClassless(unittest.TestCase):
    def test_class_returns_same(self):
        self.assertEqual(converter.converter('192.168.0.0/24'),
                         ['192.168.0.0/24'])

    def test_classless_returns_classes(self):
        self.assertEqual(converter.converter('192.168.0.0/23'),
                         ['192.168.0.0/24', '192.168.1.0/24'])
        self.assertEqual(converter.converter('192.168.0.0/30'),
                         ['192.168.0.0/32', '192.168.0.1/32',
                          '192.168.0.2/32', '192.168.0.3/32'])


class TestSubnetGeneratorToList(unittest.TestCase):
    subnets_generator = netaddr.IPNetwork('192.168.0.0/23').subnet(24)

    def test_returns_list_of_strings(self):
        self.assertEqual(converter._generator_to_list(self.subnets_generator),
                         ['192.168.0.0/24', '192.168.1.0/24'])


if __name__ == '__main__':
    unittest.main()
