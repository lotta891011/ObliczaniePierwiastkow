import unittest
import main

class MyTestCase(unittest.TestCase):
    def test_RowKwa_1Pierwiastek(self):
        self.assertEqual(main.RowKwa(1,-2,1), True)

    def test_RowKwa_2Pierwiastki(self):
        self.assertEqual(main.RowKwa(-40,4,6), True)

    def test_RowKwa_0Pierwiastków(self):
        self.assertRaises(ValueError, main.RowKwa,40,4,6)

if __name__ == '__main__':
    unittest.main()
