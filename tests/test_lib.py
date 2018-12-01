import os
import sys
import unittest
from libs.lib import struct, newAction, newIcon, addActions, fmtShortcut, generateColorByText

class TestLib(unittest.TestCase):

    def test_generateColorByGivingUniceText_noError(self):
        res = generateColorByText(u'\u958B\u555F\u76EE\u9304')
        self.assertEqual(res.green(), 53)
        self.assertEqual(res.red(), 131)
        self.assertEqual(res.blue(), 227)

if __name__ == '__main__':
    unittest.main()
