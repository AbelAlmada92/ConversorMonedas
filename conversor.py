#Conversor de varios tipos de monedas

def menu () :
    print ("1. Dolar")
    print("2. Dolar canadiences")
    print("3. Euro")
    print("4. Libra esterlina")
    print("5. Bitcoin")
    print("Cuanto desea cambiar de tu moneda ? ")
    global moneda 
    moneda = input()
    moneda = float (moneda)
    
    print("Que tipo de cambio desea elegir? ")
    global cambio
    
    cambio = input()
    cambio = int (cambio)
 
# Elegir el tipo de cambio por medio de su funcion 
    if(cambio == 1):
        dolares()
        
    elif(cambio == 2):
        dolar_can()
    
    elif(cambio == 3):
        euro()
        
    elif(cambio == 4):
        libra()
        
    elif(cambio == 5):
        bitcoin()
        
    else:
        print("El tipo de cambio que ha seleccionado no es valido.")
    
    print("Desea realizar otro tipo de cambio (si/no)?")
    global resp
    resp = input()
    resp = resp.lower()
    volver()
        
#Definir a la funcion dolares
def dolares():
    print("Ingrese el valor del dolar en su pais hoy: ")
    global precioD
    precioD = input()
    precioD = float(precioD)
    conver = moneda/precioD
    print("Usted tiene", conver, "Dolares")
    
#Definir a la funcion dolares canadienses
def dolar_can():
    print("Ingrese el valor del dolar canadiense en su pais hoy: ")
    global precioDC
    precioDC = input()
    precioDC = float(precioDC)
    conver = moneda/precioDC
    print("Usted tiene", conver, "Dolares canadienses")

#Definiendo a la funcion Euro
def euro():
    print("Ingrese el valor del Euro en se pais hoy: ") 
    global precioE
    precioE = input()
    precioE = float(precioE)
    conver = moneda/precioE
    print("Usted tiene", conver, "Euros")
    
#Definiendo a la funcion Libra Esterlina

def libra():
    print("ingrese el valor de la Libra esterlina en su pais hoy: ")
    global precio_lib 
    precio_lib = input()
    precio_lib = float(precio_lib)
    conver = moneda/precio_lib
    print("Usted tiene", conver, "Libras esterlinas")
    
#Definiendo a la funcion bitcoin
def bitcoin():
    print("Ingrese el valor del Bitcoin en su pais hoy: ")
    global precio_bit
    precio_bit = input()
    precio_bit = float(precio_bit)
    conver = moneda/precio_bit
    print("Usted tiene",conver, "Bitcoins")
    
#Definiendo la funcion volver para hacer otra consulta
def volver():
    while (resp != "no"):
        menu()    
          
#Llamado de funcion
menu()    