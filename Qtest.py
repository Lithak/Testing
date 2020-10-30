import unittest


class lernUnitTest(unittest.TestCase):
    def sampletest(self):
        num1 = 5
        num2 = 5
        self.assertNotEqual(num1, num2, "They are not Equal")


if __name__ == '__main__':
    unittest.main()

