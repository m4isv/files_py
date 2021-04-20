class Carro(object):
	nome = "fusca"
	rodas = 4
	cor = "preto"
	ano = 2016
	
	def __init__(self,portas,marca,aro):
		self.portas = portas
		self.marca = marca
		self.aro = aro
		
	
	def anda(self,km):
		print(f"carrou andou {km} kilometros ")