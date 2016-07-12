import unittest
from Calcolatrice import *

class ProvaMatrice(unittest.TestCase):
	def testSommaMatrice(self):
		matrice1="matrice1"
		matrice2="matrice2"
		self.assertEqual(sommaMatrice(matrice1, matrice2),[[0,0,0],[0,0,0],[0,0,0]])
	
unittest.main()