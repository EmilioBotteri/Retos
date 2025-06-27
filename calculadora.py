"""
🎉 Pregunta de la Semana @everyone  🚀
💡 ¡Crea tu propia calculadora con superpoderes! 🧮⚡

Queremos que construyas una función en Python que reciba dos números y una operación (suma, 
resta, multiplicación o división) y devuelva el resultado… pero con control de errores incluido.

🔹 Pregunta:
¿Cómo harías una función que pueda:

Recibir dos números y una operación ("+", "-", "*", "/")
Realizar la operación correspondiente
Controlar errores como divisiones por cero, tipos no válidos o símbolos desconocidos
Devolver mensajes útiles si algo va mal

✍️ Pistas para investigar:
¿Cómo se usan los bloques try, except, else y finally en Python?
¿Cómo puedes lanzar un error personalizado con raise?
¿Qué pasa si el usuario pasa una letra en lugar de un número?

🎯 Puntos Extra:
✅ Si usas funciones bien estructuradas.
✅ Si controlas mínimo 3 tipos de error distintos.
✅ Si devuelves mensajes claros para el usuario.
✅ Si incluyes algunos test o ejemplos de uso.
"""

while True:
    operacion = input("Selecione la operacion a realizar {+, -, *, /}: ")
    if operacion != "+" and operacion != "-" and operacion != "/" and operacion != "*":
        print("Simbolo de la operacion incorrecta")
        break 
    if operacion == "+":
        try:
            nro1 = int(input("Ingrese el primer numero: "))
            nro2 = int(input("Ingrese el segundo numero: "))
            print(nro1 + nro2)
        except:
            print("No se pudo realizar la operacion, Ingrese solo numeros")
        else:
            print("El calculo se realizo con exito")
    elif operacion == "-":
        try:
            nro1 = int(input("Ingrese el primer numero: "))
            nro2 = int(input("Ingrese el segundo numero: "))
            print(nro1 - nro2)
        except:
            print("No se pudo realizar la operacion, Ingrese solo numeros")
        else:
            print("El calculo se realizo con exito")
    elif operacion == "*":
        try:
            nro1 = int(input("Ingrese el primer numero: "))
            nro2 = int(input("Ingrese el segundo numero: "))
            print(nro1 * nro2)
        except:
            print("No se pudo realizar la operacion, Ingrese solo numeros")
        else:
            print("El calculo se realizo con exito")
    else:
        try:
            nro1 = int(input("Ingrese el primer numero: "))
            nro2 = int(input("Ingrese el segundo numero: "))
            print(nro1 / nro2)
        except ZeroDivisionError:
            print("No se puede dividir por cero, no se pudo realizar la operacion")
        except:
            print("No se pudo realizar la operacion, Ingrese solo numeros")
        else:
            print("El calculo se realizo con exito")
    pregunta = input(("Quieres realizar otra operacion?(Escriba si o no): "))
    if pregunta.lower() == "si":
        continue
    elif pregunta.lower() == "no":
        print("Nos vemos")
        break
    else:
        print("Respuesta incorrecta")
        