def cor(a = "\033[1;31;44m"):
	print(a)

def fcor(b ="\033[m"):
	print(b)
	
try:
	while True:
		cidade = int(input("\033[4;34;46mdigite o DDD:\033[m "))
		if cidade == 11:
			cor()
			print("São paulo Sp")
			fcor()
		
		elif cidade ==12:
			cor()
			print("interior de sp")
			fcor()
			
		elif cidade == 13:
			cor()
			print("Santos Sp")
			fcor()
		
		elif cidade == 14:
			cor()
			print("Bauru Sp")
			fcor()
		
		elif cidade == 15:
			cor()
			print("Sorocaba Sp")
			fcor()
		
		elif cidade == 16:
			cor()
			print("Ribeirão Preto Sp")
			fcor()
		
		elif cidade == 17:
			cor()
			print("São José do Rio Preto Sp")
			fcor()
		
		elif cidade == 18:
			cor()
			print("Presidente Prudente Sp \033[m")
			fcor()
		
		elif cidade == 19:
			cor()
			print("Campinas Sp")
			fcor()
		
		elif cidade == 21:
			cor()
			print("Rio de Janeiro RJ \033[m")
			fcor()
			
		elif cidade == 22:
			cor()
			print("Campo de Goytacazes RJ \033[m")
			fcor()
		
		
			
			
		else:
			print("\033[1;31;44m nao achei \033[m")
		
		resposta = str(input("quer continuar sim ou nao: "))
	
		if resposta[0].lower() in "n":
			print("terminou")
			break
	
		else:
			continue

except:
	print("ocorreu um error Não Achei")