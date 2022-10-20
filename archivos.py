'''
Camarillo Velazquez Diego Apolinar
Fecha: 19/Oct/22
Descripción: imprimir lineas de otro documento  

'''
file = open("devices.txt", "r")

for line in file:
    line = line.strip()
    dispositivo =  input("Dime el dispositivo a encontrar: ")
        
if dispositivo in line:
    print(line)
else:
    print("Dispositivo no encontrado")
            

file.close()
