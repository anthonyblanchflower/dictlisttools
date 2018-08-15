from __future__ import absolute_import

import unittest

import dictlisttools


class DictListToolsTests(unittest.TestCase):
    def test_sortbykey(self):
        result = dictlisttools.sortbykey([{'A': 3}, {'A': 1}, {'A': 2}], 'A')
        expected = [{'A': 1}, {'A': 2}, {'A': 3}]

        self.assertEqual(expected, result)
