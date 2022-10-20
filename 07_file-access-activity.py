file = open("devices.txt", "a")
while True:
    newItem = input("Nombre del dispositivo: ")
    if newItem == "exit" or "Exit":
        break
    file.write(newItem + "\n")
    print("All done!")
file.close()

    
        
    