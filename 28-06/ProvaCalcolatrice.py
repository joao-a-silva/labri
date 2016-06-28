import unittest
from Calcolatrice import *

class ProvaCalcolatrice(unittest.TestCase):
	def testSommaVettore(self):
		vettore=[1,2,3]
		self.assertEqual(sommaVettore(vettore),6)

unittest.main()