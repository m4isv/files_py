import bz2

data = "ola mundo virus virus"

with bz2.open("myfile.bz2", "wb") as f:
	f.write(data)