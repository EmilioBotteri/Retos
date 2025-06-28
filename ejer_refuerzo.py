
# Ejercicio 1 
# Escribir un programa que pregunte por consola por los  productos  de  una  cesta  de  la  compra,  
# separados  por  comas,  y  muestre  por  pantalla  cada  uno  de  los  productos  en  una  línea  distinta. 


def lista_productos():
    prod = input("Ingrese todos los productos separados por una coma: ")
    texto_sep = prod.split(",")
    for i in texto_sep:
        print(i.strip())




# Ejercicio 2 
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo  
# introduzca  muestre  por  pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en 
# mayúsculas  y <n> es el número de letras que tienen el nombre. 

def nombre():
    name = input("Introduzca su nombre completo: ")
    nombre_limpio = name.replace(",", "").replace(" ", "")
    print(f"El nombre {name.upper()} tiene {len(nombre_limpio)} letras")




# Ejercicio 3 
# Escribir un programa que pida al usuario dos números enteros y  muestre por pantalla la <n> entre <m> da un 
# cociente <c>  y un resto <r> donde <n> y <m> son los números introducidos  por el usuario, y <c> y <r> son el 
# cociente y el resto de la división  entera respectivamente. 


def numbers():

    try:
        n = int(input("Ingrese el 1º numero entero: "))
        m = int(input("Ingrese el 2º numero entero: "))
        c = n // m
        r = n % m
        print(f"La division entre {n} y {m} es igual a {c} y el resto es {r}.")
    except ValueError:
        print("No ha ingresado dos numero enteros validos.")
    except ZeroDivisionError:
        print("No se puede dividir por cero.")




# Ejercicio 4 
# Imagina  que  acabas  de  abrir  una  nueva  cuenta  de  ahorros  que  te ofrece el 4% de interés al año. 
# Estos ahorros debido a  intereses, que no se cobran hasta finales de año, se te añaden al  balance final de 
# tu cuenta de ahorros. Escribir un programa que  comience leyendo la cantidad de dinero depositada en la cuenta 
# de  ahorros,  introducida  por  el  usuario.  Después  el  programa  debe calcular y mostrar por pantalla la 
# cantidad de ahorros tras  el primer, segundo y tercer años. Redondear cada cantidad a dos decimales. 
 
def cuenta_ahorro(saldo_inicial:int):

    one_year = round(saldo_inicial * 1.04, 2)
    second_year = round(one_year * 1.04, 2)
    third_year = round(second_year * 1.04, 2)
    
    print(f"El ahorro total pasado un año es de: {one_year}")
    print(f"El ahorro total pasado dos años es de: {second_year}")
    print(f"El ahorro total pasado tres años es de: {third_year}")



# Con bucle para no repetir codigo:

def cuenta_ahorro(saldo_inicial):

    count = 0
    while count < 4:
        print(f"La cantidad de ahorro el {count} año(s) es de {round(saldo_inicial * 1.04 ** count, 2) }")
        count += 1



# Ejercicio 5 
# Una panadería vende barras de pan a 3.49€ cada una. El pan que  no  es  el  día  tiene  un  descuento  del  60%. 
# Escribir  un  programa  que comience leyendo el número de barras vendidas que no son  del día. Después el 
# programa debe mostrar el precio habitual de  una barra de pan, el descuento que se le hace por no ser fresca 
# y el coste final total. 


def barras_de_pan():

    precio_unitario = 3.49
    descuento = 0.6
    precio_ayer = precio_unitario * (1 - descuento)
    print(f"Precio barra fresca: {precio_unitario} €")
    print(f"Descuento por barra no fresca: {precio_unitario * descuento} €")

    try:
        hoy = int(input("Cuantas barras del dia de hoy desear llevar?: "))
        ayer = int(input("Cuantas barras del dia de ayer de desear llevar?: "))
        if hoy < 0 or ayer < 0:
            print("No se admiten numero negativos")
            return
        else:
            print(f"El importe total es de {round(hoy * precio_unitario + ayer * precio_ayer, 2)} €")

    except ValueError:
        print("El numero debe ser un numero entero")

