import unittest
from operaciones import Operaciones
ejecutar():



class tesOp(unittest.TestCase):
    def testOp(self):
        """Se espera que retorne algo"""
        self.assertEqual(obj1("suma", 1))
        self.assertEqual(obj1(None), None)

if __name__ == '__main__':
    unittest.main()
