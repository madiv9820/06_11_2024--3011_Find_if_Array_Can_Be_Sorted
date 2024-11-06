from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testCases = {1: ([8,4,2,30,15], True), 2: ([1,2,3,4,5], True), 3: ([3,16,8,4,2], False)}
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        nums, output = self.__testCases[1]
        result = self.__obj.canSortArray(nums = nums)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case2(self):
        nums, output = self.__testCases[2]
        result = self.__obj.canSortArray(nums = nums)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case2(self):
        nums, output = self.__testCases[3]
        result = self.__obj.canSortArray(nums = nums)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()