import socket
import glob


server  = socket.socket()

host = "127.0.0.1" 

port = 555

server.connect((host,port))

print(server.recv(1024))

for file in glob.iglob("*.txt"):
	print(file.encod())
	
server.send(file)


server.close()

import glob
for file in glob.iglob("/storage/emulated/0/Download/*.jpeg"):
	print(file)
