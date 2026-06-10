from Clientes import *

#Tipo de Producto
def TipoProducto(name):
    name = input('Ingrese tipo de util escolar: ')
    name = name.replace(' ','')
    name = name.lower() 
    return name 

#Marca del Producto
def MarcaProducto(nom):
    nom = input('Ingrese marca de util escolar: ')
    nom = nom.replace(' ','')
    nom = nom.lower()
    return nom

#Ingreso de DNI
def Dni(dni):
    while True:
        try:
            dni = int(input('Ingrese N° DNI: '))
                            
            if dni >= 10000000 and dni <= 99999999:
                dni = str(dni)
                break
            else:
                print('Faltan digitos')
        except ValueError:
            print('Ingrese un número por favor')
    return dni

#Busca si el dni ingresado esta en el diccionario clientes
def RepeDNI(thedni):
    return thedni in clientes

