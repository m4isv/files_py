import time,shutil

print("""
\033[1;32m╔═══╗╔╗─╔╗╔════╗╔═══╗╔╗───╔══╗╔═╗╔═╗╔═══╗╔═══╗
║╔═╗║║║─║║║╔╗╔╗║║╔═╗║║║───╚╣─╝║║╚╝║║║╔═╗║║╔═╗║
║║─║║║║─║║╚╝║║╚╝║║─║║║║────║║─║╔╗╔╗║║╚═╝║║║─║║
║╚═╝║║║─║║──║║──║║─║║║║─╔╗─║║─║║║║║║║╔══╝║╚═╝║
║╔═╗║║╚═╝║──║║──║╚═╝║║╚═╝║╔╣─╗║║║║║║║║───║╔═╗║
╚╝─╚╝╚═══╝──╚╝──╚═══╝╚═══╝╚══╝╚╝╚╝╚╝╚╝───╚╝─╚╝\033[m""")
print("\033[1;45mapp online\033[m")
print("\033[1;33mo App vai limpa a Pasta\033[m")
print("\033[7;33m org.telegram.messenger/cache\033[m")
print("\033[1;44mautomaticamente acada 30 minutos\033[m")


def limpar():
	try:
		a = shutil.rmtree("/storage/emulated/0/Android/data/org.telegram.plus/cache")
	
	except :
		print("\033[1;45ma pasta ja foi limpa\033[m")
		
	else:
		print("\033[45mapasta cache do telegram foi limpa para libera memoria...\033[m")
	

while True:
	for tempo in range(1800+1):
		time.sleep(1)
	
		if (tempo == 1800):
			print("a pasta foi limpa")
			limpar()
		continue
