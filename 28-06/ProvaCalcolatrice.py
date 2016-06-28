import unittest
from Calcolatrice import *

class ProvaCalcolatrice(unittest.TestCase):
	def testSommaVettore(self):
		vettore=[1, 2, 3]
		self.assertEqual(sommaVettore(vettore),6)
	def testSommaVettore2(self):
		vettore=[1, 5.5, 2]
		self.assertEqual(sommaVettore(vettore), 8.5)
	def testSommaVettore3(self):
		vettore=[5, 4]
		self.assertEqual(sommaVettore(vettore), 9)
unittest.main()