import unittest

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


if __name__ == '__main__':
    unittest.main()
