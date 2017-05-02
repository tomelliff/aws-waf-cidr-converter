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

    def test_ip6_class_returns_same(self):
        self.assertEqual(converter.converter('fe80::dead:beef/64'),
                         ['fe80::dead:beef/64'])

    def test_ip6_classless_returns_classes(self):
        self.assertEqual(converter.converter('fe80::dead:beef/63'),
                         ['fe80::/64', 'fe80:0:0:1::/64'])


class TestSubnetGeneratorToList(unittest.TestCase):
    subnets_generator = netaddr.IPNetwork('192.168.0.0/23').subnet(24)

    def test_returns_list_of_strings(self):
        self.assertEqual(converter._generator_to_list(self.subnets_generator),
                         ['192.168.0.0/24', '192.168.1.0/24'])


class TestGetAllowedPrefixes(unittest.TestCase):
    def test_ip4_returns_ip4_prefixes(self):
        self.assertEqual(converter.get_allowed_prefixes(4),
                         [8, 16, 24, 32])

    def test_ip6_returns_ip6_prefixes(self):
        self.assertEqual(converter.get_allowed_prefixes(6),
                         [16, 24, 32, 56, 64, 128])

    def test_wrong_ip_version_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            converter.get_allowed_prefixes(5)

        self.assertTrue('ip_version should be either 4 or 6' in
                        context.exception)


if __name__ == '__main__':
    unittest.main()
