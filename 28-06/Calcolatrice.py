
def sommaVettore(vettore):
	somma = 0

	for numero in vettore:
		somma = somma + numero

	return somma

def sommaMatrice(matrice1, matrice2):
	file1 = None

	try:
		file1 = open(matrice1, "r")
	except Exception, e:
		print ("Erro 2")
	file2 = open(matrice2, "r")


	matriceRisultato=[]
	
	for linea in file1:
		valores1=linea.replace("\n","").split(",")
		valores2=file2.readline().replace("\n","").split(",")
		vettoreSomma=[]
		print valores2
		print valores1	
		for i in range(0, 3):
			vettoreSomma.append(int(valores1[i])+int(valores2[i]))
		matriceRisultato.append(vettoreSomma)
	file1.close()
	file2.close()
	return matriceRisultato