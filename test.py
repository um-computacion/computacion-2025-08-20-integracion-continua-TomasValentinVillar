"""
modulo que contedrá los test
"""
import unittest
from main import suma, resta

class TestPrueba(unittest.TestCase):
    """
    clase de para los test
    """

    def test_suma(self):
        """
        test para funcion suma
        """
        self.assertEqual(suma(2, 3), 5)
    def test_resta(self):
        """
        test para funcion resta
        """
        self.assertEqual(resta(5, 3), 2)

if __name__ == "__main__":
    unittest.main()
