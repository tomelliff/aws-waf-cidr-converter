from __future__ import print_function
import ipaddress
import sys
import unittest

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

try:
    from io import StringIO
except ImportError:
    from StringIO import StringIO

import converter


class TestConvertCIDRRange(unittest.TestCase):
    def test_ip4_allowed_range_returns_same(self):
        self.assertEqual(converter.converter(u'192.168.0.0/24'),
                         ['192.168.0.0/24'])

    def test_ip4_range_returns_allowed_range(self):
        self.assertEqual(converter.converter(u'192.168.0.0/23'),
                         ['192.168.0.0/24', '192.168.1.0/24'])
        self.assertEqual(converter.converter(u'192.168.0.0/30'),
                         ['192.168.0.0/32', '192.168.0.1/32',
                          '192.168.0.2/32', '192.168.0.3/32'])

    def test_ip6_allowed_range_returns_same(self):
        self.assertEqual(converter.converter(u'fe80::/64'),
                         ['fe80::/64'])

    def test_ip6_range_returns_allowed_range(self):
        self.assertEqual(converter.converter(u'fe80::/63'),
                         ['fe80::/64', 'fe80:0:0:1::/64'])


class TestSubnetGeneratorToList(unittest.TestCase):
    subnets_generator = ipaddress.ip_network(u'192.168.0.0/23').subnets(
                            new_prefix=24)

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
                        str(context.exception))


class TestCommandLineHandler(unittest.TestCase):
    def test_prints_ranges_to_stdout(self):
        sys.argv[1] = u'192.168.0.0/23'
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            converter.command_line_handler()
            self.assertEqual(fakeOutput.getvalue().strip(),
                             '192.168.0.0/24\n192.168.1.0/24')


if __name__ == '__main__':
    unittest.main()
