import unittest

import converter


class TestConvertClassless(unittest.TestCase):
    def test_class_returns_same(self):
        self.assertEqual(converter.converter('192.168.0.0/24'),
                         ['192.168.0.0/24'])


if __name__ == '__main__':
    unittest.main()
