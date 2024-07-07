import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 2]
        result = sum(data)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()

# The test results from the tests I ran show that the tests are working
# and that the sum function is working. I tested multiple instances that I
# knew the answers/outputs to and was able to determine that everything was tested
# correctly and that the tests function correctly.