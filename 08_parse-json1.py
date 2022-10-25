'''
Camarillo Velázquez Diego Apolinar
Fecha: 25/Oct/22
Descripción: Parsear APIs en python

'''

import urllib.parse
import requests 

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "México"
key= "R0KOmb1NyYTPBGqyKnyO0DI5iAjpKi9k"
dest = "U.S.A"
url = main_api + urllib.parse.urlencode ({"key":key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data) 


