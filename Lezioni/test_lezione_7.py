import unittest
from lezione_7 import somma

#Testing
class TestSomma(unittest.TestCase):

    def test_somma(self):
        self.assertEqual(somma(1,1),2)
        self.assertEqual(somma(1.5,2.5),4)