
saludo = ["Hola, me llamo mate, como TO-MATE pero sin el TO",
          "Buen dia, has desayunado? Yo desayuno perdedores",
          "Alo, soy el rayo McQueen, no me agrada que insulten de esa manera a mi amigo",
          "Que onda, necesitas pintura hermano, Ramon te pinta bien",
          "Hola quien eres? Yo no soy Mack soy Peterbilt ignorante, enciende las luces salvaje"
         ]
claves_saludo = ["hola", "como andas", "como estas", "todo bien", "que tal", "buen dia",
                 "buenas tardes", "buenas noches", "que onda", "buenas", "como va",]


despedirse = ["Adios para Radiador Springs y adios para Bessie. California aqui vooy",
              "Vuela alto Staly, se libree",
              "Adios y recuerda, volar cual cohete, atacar como bólido",
              "Vamonos, yo soy Mate Tomate, el que con guuuusto te lleva",
              "Nos vemos, se feliz, mas feliz que un politico en navidad",
              "Te vere en la linea de meta amigo, chau cuchauuu!"
             ]
claves_despedida = ["chau", "gracias", "adios", "nos vemos", "hasta luego", "hasta ahora",
                    "hasta pronto", "que vaya bien", "me voy"]

carrera = ["Los coches de carrera no tienen luces, porque la pista tiene luces",
           "Queeee, un copa piston..... Dos copas PISTON?",
           "Aqui voy, velocidad, soy veloz.. un ganador, cuarenta perdedores ",
           "Gira a la derecha e iras a la izquierda",
           "No tan rapido macquine... No tan rapido? Es tu nuevo lema quizas?",
           "Lo que pasa es que, el trueno llega siempre despues del rayo",
           "La vida es una carrera, disfruta del trayecto"
          ]
claves_carrera = ["ganar", "coche", "carrera", "pista", "competencia", "ganador", "auto",
                  "corredor","veloz", "velocidad", "tiempo", "motor", "puesto", "lugar", "circuito"]

amigo = ["A rayo le gusta sallyy, McQuenn y Sally se fueron a pasear y entonces no se que cantar",
         "Sabia, hice una buena eleccion ... Mi mejor amigo",
         "Un viejo amigo corredor gruñon me dijo algo, son solo copas vacias",
         "Chi trova un amico trova un tesoro",
        ]
claves_amigo = ["amigo", "novio", "novia", "amistad", "amigos","amiga"]

defecto = ["Use Rust-eze, y usted... ¡lucirá como yo! Cuchaaau",
            "Y la pregunta es:¿Donde esta McQueen?",
            "Son palabras rudas que vienen de un coche taaan fragil",
            "Reeeetrovisores, no necesito saber a donde voy, solo saber donde he estado",
            "Guuau este combustible organico es delicioso hermano",
            "Voltear tractores es divertido. Pero que frank no te atrape",
            "Ohh helado de pistacho, NO NO Wasabi. sisi, ponme mas no seas tacaño",
            "Si sigues hablando solo van a pensar que estas loco"
            ]

pregunta_asistente = ["En que te ayudo?: ", "Que nececitas?: " ,"Que deseas?: ", 
                      "Como te puedo ayudar?: ", "¿Que precisas?: "]

import random

def asistente(mensaje:str):
    mensaje = mensaje.lower()

    if any(palabra in mensaje.lower() for palabra in claves_saludo):  
        return random.choice(saludo)
    elif any(palabra in mensaje.lower() for palabra in claves_despedida):
        return random.choice(despedirse)
    elif any(palabra in mensaje.lower() for palabra in claves_carrera):
        return random.choice(carrera)
    elif any(palabra in mensaje.lower() for palabra in claves_amigo):
        return random.choice(amigo)
    else:
        return random.choice(defecto)


print("Cuando quieras terminar escribe: salir")
while True:
    mensaje = input(random.choice(pregunta_asistente)).lower()
    if mensaje == "salir":
        print("Nos vemos en el proximo Grand Prix!")
        break
    
    print(asistente(mensaje))

