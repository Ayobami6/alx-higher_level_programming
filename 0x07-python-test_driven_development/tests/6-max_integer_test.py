"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """ Testing for empty list
        """
        test_param = []
        result = max_integer(test_param)
        self.assertEqual(result, None)

    def test_max_int(self):
        """ Testing the function for max integer
        """
        test_param = [1, 4, 6]
        result = max_integer(test_param)
        self.assertEqual(result, 6)

    def test_max_int_mid(self):
        """ Testing the function for max integer
        """
        test_param = [1, 6, 4]
        result = max_integer(test_param)
        self.assertEqual(result, 6)

    def test_max_int_mid(self):
        """ Testing the function for max integer
        """
        test_param = [1, 6, 4]
        result = max_integer(test_param)
        self.assertEqual(result, 6)

    def test_for_string(self):
        """ Testing for strings
        """
        test_param = ""
        result = max_integer(test_param)
        self.assertEqual(result, None)

    def test_one_element(self):
        """ Testing for length 1
        """
        test_param = [3]
        result = max_integer(test_param)
        self.assertEqual(result, 3)

    def test_floats(self):
        """ Testing for floats
        """
        test_param = [2.0, 3.0,  5.0, 6.8]
        result = max_integer(test_param)
        self.assertEqual(result, 6.8)

    def test_list_of_str(self):
        test_param = ["Ayobami",  "me", "bunmi"]
        result = max_integer(test_param)
        self.assertEqual(result, "me")

    def test_neg_only(self):
        test_param = [-1, -2, -3, -10]
        result = max_integer(test_param)
        self.assertEqual(result,  -1)

    def test_one_neg(self):
        test_param = [1, 2, -3, 10]
        result = max_integer(test_param)
        self.assertEqual(result, 10)


if __name__ == "__main__":
    unittest.main()
