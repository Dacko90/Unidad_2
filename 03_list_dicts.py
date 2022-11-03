'''
Camarillo Velazquez DIego 
Fecha: 13 OCt 2022
Descripción: Imprimir informacion personal

'''
#Esta variable se asigno para imprimir el texto y concatenar un espacio sin poner un espacio en la cadena de texto
space = " "

print("¿Como te llamas?:")
name = input()
print("¿Cual es tu apellido?:")
lastn = input()
print("¿De donde eres?:")
location = input()
print("¿Cual es tu edad?:")
age = input()


print ("Se llama"+ space + name + space +"y su apellido es"+ space + lastn +space+ "es originario de"+ space + location +space+ "y tiene"+space + age +space+ "años.")
