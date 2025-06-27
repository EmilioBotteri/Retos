

"""
🎉 Pregunta de la Semana @everyone  🚀
💡 ¡Tu edad en segundos! ⏳

El tiempo pasa volando… pero, ¿alguna vez has calculado tu edad en segundos? 🤯

🔹 Pregunta:
Usando la librería datetime, ¿cómo calcularías cuántos segundos has vivido desde tu fecha de nacimiento?

✍️ Pistas para empezar:

¿Cómo puedes obtener la fecha de hoy con datetime?

¿Cómo restarías tu fecha de nacimiento de la fecha actual?

¿Cómo convertirías esa diferencia a segundos?

🎯 Puntos Extra:
✅ Si calculas también tu edad en minutos y horas.
✅ Si agregas una función para calcularlo con cualquier fecha de nacimiento.
✅ Si comparas cuántos segundos han vivido algunos personajes históricos.

🔥 ¡Atrévete a calcularlo y sorpréndete con el resultado! ⏰🎂."
"""

from datetime import datetime

def calcular_edad(año:int, mes:int, dia:int, hora:int, minuto:int):

    fecha_nacimiento = datetime(año, mes, dia, hora, minuto)
    dif = datetime.now() - fecha_nacimiento
    
    print(f"Tu edad en segundos es: {dif.total_seconds()} seg.")
    print(f"En minutos es: {dif.total_seconds() / 60} min.")
    print(f"O en horas es: {dif.total_seconds() / 3600} hs.")
    print(f"Y tus dias de vida son: {dif.total_seconds() / 86400} dias.")


calcular_edad(2001, 1, 25, 18, 45)