import unittest
import main

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(main.add(2, 3), 5)
        self.assertEqual(main.add(-10, 5), -5)
        self.assertEqual(main.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(main.subtract(10, 3), 7)
        self.assertEqual(main.subtract(5, 10), -5)
        self.assertEqual(main.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(main.multiply(2, 3), 6)
        self.assertEqual(main.multiply(-5, 4), -20)
        self.assertEqual(main.multiply(0, 10), 0)

    def test_modulo(self):
        self.assertEqual(main.modulo(10, 3), 1)
        self.assertEqual(main.modulo(17, 5), 2)
        self.assertEqual(main.modulo(100, 7), 2)

if __name__ == '__main__':
    unittest.main()
