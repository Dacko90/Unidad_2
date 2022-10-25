'''
Camarillo Velázquez Diego Apolinar
Fecha: 25/Oct/22
Descripción: Parsear APIs en python

'''

import urllib.parse
import requests 

while True:
    orig = input("Starting Location: ")
    dest = input("Destination: ")
    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    key= "R0KOmb1NyYTPBGqyKnyO0DI5iAjpKi9k"
    url = main_api + urllib.parse.urlencode ({"key":key, "from":orig, "to":dest})
    
    print("URL: " + (url))


    
