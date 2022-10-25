'''
Camarillo Velázquez Diego Apolinar
Fecha: 25/Oct/22
Descripción: Parsear APIs en python

'''

import urllib.parse
import requests 

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    key= "R0KOmb1NyYTPBGqyKnyO0DI5iAjpKi9k"
    url = main_api + urllib.parse.urlencode ({"key":key, "from":orig, "to":dest})

    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + str(json_data["route"]["formattedTime"]))
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("=============================================")
    