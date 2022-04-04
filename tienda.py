productos=[]
opcion=1

while(opcion !=0):
    producto={}
    opcion=int(input("Digite una opcion: "))
    if(opcion==1):
        producto['codigo']=input("Digite el codigo del producto ")
        producto['nombre']=input("Digite el nombre del producto ")
        producto['precio']=int(input("Digite el precio del producto "))
        productos.append(producto)
        
    elif(opcion==2):
        print(productos)
    elif(opcion==3):
        print("")
    else:
        print("")
