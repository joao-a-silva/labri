import unittest
from Calcolatrice import *

class ProvaMatrice(unittest.TestCase):
	def testSommaMatrice(self):
		matrice1="Matrice1"
		matrice2="Matrice2"
		self.assertEqual(sommaMatrice(matrice1, matrice2),[[0,0,0],[0,0,0],[0,0,0]])
	
unittest.main()