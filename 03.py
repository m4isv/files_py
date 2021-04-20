try:
	n1 = int(input("digitr um numero\n"))
	
	n2 = int(input("digitr um numero\n"))
	
	soma = n1 + n2
	
	print(f"a soma entre \033[1;33m{n1} e {n2}\033[m e \033[1;31;43m{soma}\033[m")
	
except:
	print("\033[1;31;44mocorreu um error\033m")