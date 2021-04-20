#gerador de pessoas
import requests

api =  requests.get("https://brasikkkk.000webhostapp.com/pessoas.php").json()

for base1 in api:
  print(f"》[{base1}]\n》[{api[base1]}]")