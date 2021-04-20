nome = str(input("digite Seu Nome Completo\n")).strip()

print("Analizando Seu nome....")

print("Seu nome em Maiuscula e {}".format(nome.upper()))

print("Seu nome em Minuscula e {}".format(nome.lower()))

print("Seu nome Tem Ao todo {} Letras".format(len(nome) - nome.count(" ")))

print("Seu primeiro Nome tem {} letras".format(nome.find(" ")))

