#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for unittest of max_integer program"""

    def test_documentation(self):
        self.assertTrue(len(__import__("6-max_integer").__doc__) > 0)

        self.assertTrue(len(max_integer.__doc__) > 0)

    def test_positives(self):
        """Testing positive numbers"""

        test_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(test_list), 4)

        test_list = [1, 2, 4, 3]
        self.assertEqual(max_integer(test_list), 4)

        test_list = [4, 4, 4, 4]
        self.assertEqual(max_integer(test_list), 4)

        test_list = [1, 2, 4, 4]
        self.assertEqual(max_integer(test_list), 4)

        test_list = [1.1, 2.2, 3.3, 4.4]
        self.assertEqual(max_integer(test_list), 4.4)

        test_list = [4, 4.1, 4.12, 4.22]
        self.assertEqual(max_integer(test_list), 4.22)

        test_list = [1000, 1, 2, 3]
        self.assertEqual(max_integer(test_list), 1000)

        test_list = [1, 1000, 2, 3]
        self.assertEqual(max_integer(test_list), 1000)

        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(max_integer(test_list), 15)

        test_list = [15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.assertEqual(max_integer(test_list), 15)

        test_list = [15]
        self.assertEqual(max_integer(test_list), 15)

        test_list = [[1, 2, 3, 4], [4, 3, 2, 1]]
        self.assertEqual(max_integer(test_list), [4, 3, 2, 1])

        test_list = (1, 2, 3, 4)
        self.assertEqual(max_integer(test_list), 4)

        test_list = ((1, 2, 3, 4), (4, 3, 2, 1))
        self.assertEqual(max_integer(test_list), (4, 3, 2, 1))

        test_list = ["Derek", "Kwok"]
        self.assertEqual(max_integer(test_list), "Kwok")

    def test_negatives(self):
        """Testing negative numbers"""

        test_list = [-2, 0, 2, 4]
        self.assertEqual(max_integer(test_list), 4)

        test_list = [-7, -6, -5, -4]
        self.assertEqual(max_integer(test_list), -4)

        test_list = [-4.22, -4.12, -4.10, -4.08]
        self.assertEqual(max_integer(test_list), -4.08)

    def test_none_and_zero(self):
        """Testing None and zeros"""

        test_list = []
        self.assertEqual(max_integer(test_list), None)

        test_list = [0, 0, 0, 0]
        self.assertEqual(max_integer(test_list), 0)

        self.assertEqual(max_integer(), None)

        test_list = {}
        self.assertEqual(max_integer(test_list), None)

        test_list = ()
        self.assertEqual(max_integer(test_list), None)

        self.assertEqual(max_integer(), None)

    def test_not_list(self):
        """Testing incorrect data types"""

        test_list = [1, 2, "Derek", 4]
        self.assertRaises(TypeError)

        test_list = [1, 2, [1, 2, 3], 4]
        self.assertRaises(TypeError)

        test_list = [1, 2, (1, 2, 3), 4]
        self.assertRaises(TypeError)

        test_list = 5
        self.assertRaises(TypeError)

        test_list = 5.5
        self.assertRaises(TypeError)

        test_list = (1, 2, 3, 4)
        self.assertEqual(max_integer(test_list), 4)

        test_list = "Derek"
        self.assertEqual(max_integer(test_list), 'r')

        test_list = 'D'
        self.assertEqual(max_integer(test_list), 'D')

        test_list = None
        self.assertRaises(TypeError)

        test_list = {1, 2, 3, 4}
        self.assertRaises(TypeError)

if __name__ == '__main__':
    unittest.main()

