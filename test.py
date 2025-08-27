import unittest

from main import suma, resta

class TestPrueba(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
    
    def test_resta(self):
        self.assertEqual(suma(5, -3), 2)

if __name__ == "__main__":
    unittest.main()