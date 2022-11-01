import unittest

from my_calculation import sum,mul



class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1,2,3]
        result = sum(data)
        self.assertEqual(result, 7)

    def test_list_int(self):
        """
        Test that it can mul a list of integers
        """
        data = [1, 2, 4]
        result = mul(data)
        self.assertEqual(result, 8)    

    def test_array_int(self):
        """
        Test that it can sum a array of integers
        """
        data = {1, 2, 4}
        result = sum(data)
        self.assertEqual(result, 7)
    def test_tuple_int(self):
        """
        Test that it can sum a tuple of integers
        """
        data = (1, 2, 4)
        result = sum(data)
        self.assertEqual(result, 7)
    def test_negative_string(self):
        """
        Test that it can sum of a string
        """
        data = "string"
        with self.assertRaises(TypeError):
            result = sum(data)


if __name__ == '__main__':
    unittest.main()