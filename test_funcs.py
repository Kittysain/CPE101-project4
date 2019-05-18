# Project 4
#
# Name: Kitty Zhuang and Josh Zhang
# Instructor: S. Einakian
# Section: CPE101_01
####################################################


import unittest
from funcs import *

class TestCases(unittest.TestCase):
    def test_transpose(self):
        list1 = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
        list4 = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]
        list2 = [5, 6, 7, 8, 9, 5, 6, 7, 8, 9, 5, 6, 7, 8, 9, 5, 6, 7, 8, 9, 5, 6, 7, 8, 9]
        list5 = [5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9]
        list3 = [3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7]
        list6 = [3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7]
        self.assertEqual(transpose(list1), list4)
        self.assertEqual(transpose(list2), list5)
        self.assertEqual(transpose(list3), list6)

    def test_validate_cages(self):
        list1 = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
        cage1 = [[0,0,5],[6,1,2,3],[11,5,9,10]]
        list2 = [5, 6, 7, 8, 9, 5, 6, 7, 8, 9, 5, 6, 7, 8, 9, 5, 6, 7, 8, 9, 5, 6, 7, 8, 9]
        cage2 = [[10, 0, 5], [21, 1, 2, 3], [26, 5, 9, 10]]
        list3 = [3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7]
        cage3 = [[6, 0, 5], [15, 1, 2, 3], [20, 5, 9, 10]]
        self.assertTrue(validate_cages(list1,cage1))
        self.assertTrue(validate_cages(list2,cage2))
        self.assertTrue(validate_cages(list3,cage3))
        self.assertFalse(validate_cages(list1,cage3))

    def test_validate_rows(self):
        pass

    def test_validate_cols(self):
        pass

    def text_validate_all(self):
        pass
