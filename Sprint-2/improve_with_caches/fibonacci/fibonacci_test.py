import unittest

from fibonacci import fibonacci

class FibonacciTest(unittest.TestCase):
    def test_0(self):
        self.assertEqual(fibonacci(0), 0)

    def test_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_2(self):
        self.assertEqual(fibonacci(2), 1)

    def test_3(self):
        self.assertEqual(fibonacci(3), 2)

    def test_10(self):
        self.assertEqual(fibonacci(10), 55)

    def test_50(self):
        self.assertEqual(fibonacci(50), 12586269025)
    def test_200(self):
        self.assertEqual(fibonacci(200), 280571172992510140037611932413038677189525)

if __name__ == "__main__":
    unittest.main()
