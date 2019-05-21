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
        list_1 = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
        list_4 = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]
        list_2 = [5, 6, 7, 8, 9, 5, 6, 7, 8, 9, 5, 6, 7, 8, 9, 5, 6, 7, 8, 9, 5, 6, 7, 8, 9]
        list_5 = [5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9]
        list_3 = [3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7]
        list_6 = [3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7]
        self.assertEqual(transpose(list_1), list_4)
        self.assertEqual(transpose(list_2), list_5)
        self.assertEqual(transpose(list_3), list_6)

    def test_validate_cages(self):
        list1 = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
        list2 = [0, 1, 5, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
        cage1 = [[0, 0, 5], [6, 1, 2, 3], [4, 5, 9, 10]]
        cage2 = [[2, 2, 5], [4, 0, 1, 3]]
        cage3 = [[4, 0, 4], [3, 5, 6, 7]]
        cage4 = [[0, 0, 1]]
        self.assertFalse(validate_cages(list1, cage4))
        self.assertFalse(validate_cages(list2, cage2))
        self.assertTrue(validate_cages(list1, cage1))
        self.assertTrue(validate_cages(list1, cage2))
        self.assertTrue(validate_cages(list1, cage3))

    def test_validate_rows(self):
        grid1 = [4, 1, 2, 5, 3, 1, 5, 4, 3, 2, 2, 3, 5, 4, 1, 3, 4, 1, 2, 5, 5, 2, 3, 1, 4]
        grid2 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
        grid3 = [1, 2, 2, 3, 4, 4, 2, 1, 6, 2, 4, 5, 6, 7, 3, 1, 5, 7, 3, 4, 1, 2, 1, 8, 5]

        self.assertTrue(validate_rows(grid1))
        self.assertTrue(validate_rows(grid2))
        self.assertFalse(validate_rows(grid3))

    def test_validate_cols(self):
        grid11 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
        grid22 = [1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9]
        grid33 = [1, 3, 4, 5, 7, 2, 3, 2, 6, 7, 8, 2, 3, 4, 6, 1, 4, 3, 1, 7, 8, 2, 4, 6, 7]
        self.assertFalse(validate_cols(grid11))
        self.assertTrue(validate_cols(grid22))
        self.assertFalse(validate_cols(grid33))

    def test_validate_all(self):
        grid_1 = [4, 1, 2, 5, 3, 1, 5, 4, 3, 2, 2, 3, 5, 4, 1, 3, 4, 1, 2, 5, 5, 2, 3, 1, 4]
        grid_2 = [1, 2, 3, 4, 5, 3, 1, 4, 5, 2, 2, 5, 1, 3, 4, 5, 4, 2, 1, 3, 4, 3, 5, 2, 1]
        grid_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        grid_4 = [3, 5, 2, 1, 4, 5, 1, 3, 4, 2, 2, 4, 1, 5, 3, 1, 2, 4, 3, 5, 4, 3, 5, 2, 1]
        cage_1 = [[5, 0, 5], [8, 1, 2, 6], [8, 3, 8], [6, 4, 9, 14], [13, 7, 12, 13], [5, 10, 15], [14, 11, 16, 20, 21],
                 [6, 17, 18, 22], [10, 19, 23, 24]]
        cage_2 = [[4, 0, 1, 6], [8, 2, 7, 12], [14, 3, 4, 8], [15, 5, 10, 11, 15], [14, 9, 13, 14, 18, 19, 24],
                 [11, 16, 20, 21], [9, 17, 22, 23]]
        cage_3 = [[8, 1, 2, 3], [4, 7, 8, 4, 10]]
        cage_4 = [[9, 0, 5, 6], [8, 1, 2], [10, 6, 2, 13], [12, 4, 9, 12, 14, 19], [3, 7], [8, 10, 11, 15],
                 [13, 12, 18, 20, 21], [5, 13, 21], [6, 12, 20, 21]]
        self.assertTrue(validate_all(grid_1, cage_1))
        self.assertTrue(validate_all(grid_2, cage_2))
        self.assertFalse(validate_all(grid_3, cage_3))
        self.assertFalse(validate_all(grid_4, cage_4))

if __name__ == '__main__':
    unittest.main()





