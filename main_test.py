# import unittest
# import main

# class TestMain(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(main.add(2, 3), 5)
#         self.assertEqual(main.add(-10, 5), -5)
#         self.assertEqual(main.add(0, 0), 0)

#     def test_subtract(self):
#         self.assertEqual(main.subtract(10, 3), 7)
#         self.assertEqual(main.subtract(5, 10), -5)
#         self.assertEqual(main.subtract(0, 0), 0)

#     def test_multiply(self):
#         self.assertEqual(main.multiply(2, 3), 6)
#         self.assertEqual(main.multiply(-5, 4), -20)
#         self.assertEqual(main.multiply(0, 10), 0)

#     def test_modulo(self):
#         self.assertEqual(main.modulo(10, 3), 1)
#         self.assertEqual(main.modulo(17, 5), 2)
#         self.assertEqual(main.modulo(100, 7), 2)

# if __name__ == '__main__':
#     unittest.main()
from main import add, subtract, multiply, modulo

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-5, 5) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(10, 5) == 5
    assert subtract(8, 8) == 0

def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(0, 10) == 0
    assert multiply(-3, 2) == -6

def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(8, 4) == 0
    assert modulo(7, 2) == 1

# Run the tests
test_add()
test_subtract()
test_multiply()
test_modulo()
