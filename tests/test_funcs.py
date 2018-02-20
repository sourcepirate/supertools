import unittest
from functools import reduce
from supertools import smap, sfilter, sreduce

class TestAllFunctions(unittest.TestCase):

    def setUp(self):
        self._list = range(100)
    
    def test_map(self):
        func = lambda x: x*x
        self.assertListEqual(list(map(func, self._list)), smap(func, self._list))
    
    def test_filter(self):
        func = lambda x: x % 2 == 0
        self.assertListEqual(list(filter(func, self._list)), sfilter(func, self._list))
    
    def test_reduce(self):
        func = lambda x, y : x+y
        self.assertEqual(reduce(func, self._list), sreduce(func, self._list))