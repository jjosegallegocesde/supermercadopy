productos=[]
opcion=1
bandera=True

while(opcion!=0):
    producto={}
    opcion=int(input("digite una opcion: "))
    if(opcion==1):
        producto['codigo']=input("digite un codigo de producto: ")
        producto['nombre']=input("digite un nombre de producto: ")
        productos.append(producto)
    elif(opcion==2):
        print(productos)
    elif(opcion==3):
        id=input("Digite el codigo del producto: ")
        for producto in productos:
            if(producto['codigo']==id):
                bandera=True
                producto['nombre']="juan"
                print("producto editado con exito")
                break
            else:
                bandera=False
        if(bandera==False):
            print("producto no encontrado")
    elif(opcion==4):
        id=input("Digite el codigo del producto: ")
        for indice,producto in enumerate(productos):
            if(producto['codigo']==id):
                bandera=True
                productos.pop(indice)
                print("eliminando el",indice)
                break
            else:
                bandera=False
        if(bandera==False):
            print("producto no encontrado")        
            



