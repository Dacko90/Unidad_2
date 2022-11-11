import urllib.parse
import requests

url= "https://api.spoonacular.com/recipes/findByIngredients?apiKey=2ea18f4222264c80b34d37d2111487a8&ingredients=apples,+flour,+sugar&number=2"
json_data = requests.get(url).json()
#print(json_data)

titulo= json_data [0]['title']
img= json_data[0]['image']

print("===================================")
print("Titulo de la receta: "+titulo)
print("Imagen en linea de la receta: " +img)


