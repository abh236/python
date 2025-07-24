import requests

get_url="https://pokeapi.co/api/v2/"

def get_pokimon(name):
  url=f"{get_url}/pokemon/{name}"
  response=requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    print("Not Found")

data=get_pokimon('pikachu')
data1=get_pokimon('typhlosion')
print(data["name"])
print(data["id"])
print(data["height"])
print(data["weight"])
print(data1["name"])
print(data1["id"])
print(data1["height"])
print(data1["weight"])