print ("¡Cual es tu numero de ipv4? ")
acl = input()
if acl >= 1 and acl <= 99:
    print("Esta es una direccion estandar.")
elif acl >=100 and acl <= 199:
    print("Esta es una direccion extendido.")
else:
    print("Su numero no es un valor permitido de ACL.")
