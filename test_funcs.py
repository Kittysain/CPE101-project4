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
        list4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        cage4 = [[5, 1, 2, 3], [7, 5, 6, 8]]
        self.assertFalse(validate_cages(list1,cage1))
        self.assertFalse(validate_cages(list2,cage2))
        self.assertFalse(validate_cages(list3,cage3))
        self.assertFalse(validate_cages(list1,cage3))
        self.assertTrue(validate_cages(list4,cage4))

    def test_validate_rows(self):
        grid1 = [4, 1, 2, 5, 3, 1, 5, 4, 3, 2, 2, 3, 5, 4, 1, 3, 4, 1, 2, 5, 5, 2, 3, 1, 4]
        grid2 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
        grid3 = [1, 2, 2, 3, 4, 4, 2, 1, 6, 2, 4, 5, 6, 7, 3, 1, 5, 7, 3, 4, 1, 2, 1, 8, 5]
        self.assertTrue(validate_rows(grid1))
        self.assertTrue(validate_rows(grid2))
        self.assertFalse(validate_rows(grid3))

    def test_validate_cols(self):
        grid1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
        grid2 = [1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9]
        grid3 = [1, 3, 4, 5, 7, 2, 3, 2, 6, 7, 8, 2, 3, 4, 6, 1, 4, 3, 1, 7, 8, 2, 4, 6, 7]
        self.assertFalse(validate_cols(grid1))
        self.assertTrue(validate_cols(grid2))
        self.assertFalse(validate_cols(grid3))

    def test_validate_all(self):
        grid1 = [4, 1, 2, 5, 3, 1, 5, 4, 3, 2, 2, 3, 5, 4, 1, 3, 4, 1, 2, 5, 5, 2, 3, 1, 4]
        grid2 = [1, 2, 3, 4, 5, 3, 1, 4, 5, 2, 2, 5, 1, 3, 4, 5, 4, 2, 1, 3, 4, 3, 5, 2, 1]
        grid3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        grid4 = [3, 5, 2, 1, 4, 5, 1, 3, 4, 2, 2, 4, 1, 5, 3, 1, 2, 4, 3, 5, 4, 3, 5, 2, 1]
        cage1 = [[5, 0, 5], [8, 1, 2, 6], [8, 3, 8], [6, 4, 9, 14], [13, 7, 12, 13], [5, 10, 15], [14, 11, 16, 20, 21], [6, 17, 18, 22], [10, 19, 23, 24]]
        cage2 = [[4, 0, 1, 6], [8, 2, 7, 12], [14, 3, 4, 8], [15, 5, 10, 11, 15], [14, 9, 13, 14, 18, 19, 24], [11, 16, 20, 21], [9, 17, 22, 23]]
        cage3 = [[8, 1, 2, 3], [4, 7, 8, 4, 10]]
        cage4 = [[9, 0, 5, 6], [8, 1, 2], [10, 6, 2, 13], [12, 4, 9, 12, 14, 19], [3, 7], [8, 10, 11, 15], [13, 12, 18, 20, 21], [5, 13, 21], [6, 12, 20, 21]]
        self.assertTrue(validate_all(grid1, cage1))
        self.assertTrue(validate_all(grid2, cage2))
        self.assertTrue(validate_all(grid3, cage3))
        self.assertFalse(validate_all(grid4, cage4))



if __name__ == '__main__':
    unittest.main()





