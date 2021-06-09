import unittest

class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result+=num
        for num in nums:
            self.result+=num
        return self
    def subtract(self, num, *nums):
        self.result-=num
        for num in nums:
            self.result-=num
        return self

class MathDojoTests(unittest.TestCase):
    def setUp(self):
        print('init MathDojoTests')
        self.md = MathDojo()
        print('setting up MathDojo instance')
    def testOne(self):
        self.assertEqual(self.md.add(2).subtract(4).result, -2)
    def testTwo(self):
        self.assertEqual(self.md.add(24).subtract(13,3,5).add(3,5,7).result, 18)
    def testThree(self):
        self.assertEqual(self.md.add(16,72,45).subtract(24,37,64,55).add(2,4,6,8,92).subtract(1,3,5).result, 56)
    def testFour(self):
        self.assertEqual(self.md.add(73,74,75,76,76,76).subtract(110,111,110,110,111).result, -102)
    def testFive(self):
        self.assertEqual(self.md.add(2,2).subtract(3).add(5).subtract(1,2,4).result, -1)
    def tearDown(self):
        print('tearing down mathDojo tests')

if __name__ == '__main__':
    unittest.main()