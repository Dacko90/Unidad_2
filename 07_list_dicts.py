'''
Camarillo Velazquez Diego Apolinar
Fecha: 19/Oct/22
Descripción: imprimir lineas de otro documento  

'''
file = open("devices.txt", "r")
dispositivo =  input("Dime el dispositivo a encontrar: ")


for line in file:
    line = line.strip()
    
        
if dispositivo in line:
    print(line)
else:
    print("Dispositivo no encontrado")
            

file.close()
