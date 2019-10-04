#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_positives_and_negatives(self):
        self.assertEqual(max_integer([-1, 0, 9, -6789, 98, 9, -98]), 98)

    def test_deordered_nums(self):
        self.assertEqual(max_integer([3, 5, 8, 1, 4]), 8)

    def test_floats(self):
        self.assertEqual(max_integer([3.566, 1.99999999, 7.989]), 7.989)

    def test_floats_negatives(self):
        self.assertEqual(max_integer([-9.898948, -1111, -5.987]), -5.987)

    def test_repeated_numbers(self):
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_repeated_numbers_negatives(self):
        self.assertEqual(max_integer([-2, -2, -2]), -2)

    def test_emptylist(self):
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        self.assertEqual(max_integer([2]), 2)

    def test_one_element_negative(self):
        self.assertEqual(max_integer([-199999]), -199999)

    def test_words_inside_list(self):
        self.assertEqual(max_integer(["jorge"]), "jorge")

    def test_words_as_input(self):
        self.assertEqual(max_integer("jorge"), "r")

    def test_tuple_inside_list(self):
        self.assertEqual(max_integer([(1, 2, 3, 4, 5)]), (1, 2, 3, 4, 5))

    def test_multi_tuples_inside(self):
        self.assertEqual(max_integer([(1, 2, 3), (3, 2, 3)]), (3, 2, 3))

    def test_multi_tuples_inside_again(self):
        self.assertEqual(max_integer([(1, 2, 3), (0, 2, 3)]), (1, 2, 3))

    def test_multi_lists(self):
        self.assertEqual(max_integer([[1, 2, 3], [4, 2, 3]]), [4, 2, 3])

    def test_None_as_input(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_just_a_number(self):
        with self.assertRaises(TypeError):
            max_integer(5)

if __name__ == "__main__":
    unittest.main()
