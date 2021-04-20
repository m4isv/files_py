from time import sleep
def link():
	print("="*20)
c="cadastre-se no banco"
link()
print(c)
link()

nome=str(input("qual e seu nome ?\n")).upper()
print("Cadastrando aguarde...")
sleep(3)
print("usuario {} cadastrado".format(nome))
a="cadastre uma senha"
link()
print(a)
link()
senha=input("esconha uma senha\n")
print("cadastrando senha ")
print("aguarde....")
sleep(5)
link()
print("AGUARDE PARA A CONFIRMAÇÃO")
sleep(6)
for cont in range(10, -1, -1):
	print(cont)
	sleep(0.7)
print("Voce esta cadastrado no banco")
link()