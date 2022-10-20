file = open("devices.txt", "a")
while True:
    newItem = input("Nombre del dispositivo: ")
    if newItem == "exit" or "Exit":
        print("All done!")
        break
    file.write(newItem + "\n")
file.close()

    
        
    