"""
☀️ Pregunta de la Semana  @everyone – Reto de Verano 🍉
🏖️ ¡Bienvenido al Generador de Planes Vacacionales en Python! 🐍🌴

💡 Se acerca el verano y tu misión esta semana es crear un pequeño sistema en Python que genere 
un plan de vacaciones divertido y aleatorio (¡o casi!).

🔹 Reto:
Crea una función que genere un plan de vacaciones personalizado, combinando elementos de varias 
listas, como:

Destino (playa, montaña, ciudad, pueblo mágico...)
Actividad (surf, senderismo, museos, leer en una hamaca...)
Duración (3 días, 1 semana, 10 días...)
Compañía (solo, con amigos, con familia, con un gato...)
Presupuesto estimado (opcional)

🔄 Puedes hacer que el programa:

Genere un plan aleatorio cada vez o permita al usuario elegir una categoría 
(por ejemplo, solo destinos de playa)

✍️ Pistas para lograrlo:

Usa listas y funciones
Puedes usar random.choice() para seleccionar elementos

Si quieres añadir dificultad: permite que el usuario modifique las listas con sus propias opciones

🎯 Puntos Extra:
✅ Si el resultado se presenta con estilo (uso de prints decorativos, emojis, etc.)
✅ Si incluyes una opción “modo ahorro” o “modo lujo”
✅ Si agregas validaciones o personalización extra

🔥 ¡Haz que Python planifique tus vacaciones soñadas! ¿Te irás a Bali con tu perro o a una cabaña 
nórdica con libros y café? 🏕️🐶✈️
"""

# Destinos y Actividades:
beach_economy = ["🏖️ Algarve, Portugal: Barato para llegar, comida y hospedaje accesibles",
                 "🌅 Costa Brava, España: Muy lindo poco gasto en transporte",
                 "🏝️ Islas Canarias (Tenerife, Lanzarote, Gran Canaria) España: Vuelos low cost desde península",
                 "☀️ Malta: Chiquito, fácil de recorrer, buen clima casi todo el año y vuelos baratos",
                 "🌊 Kotor, Montenegro: Playas tranquilas, barato comer y dormir",
                 "🇭🇷 Zadar o Split, Croacia: Se consiguen vuelos barato si sacás con tiempo",
                 "🌴 Marrakech + Essaouira, Marruecos: Vuelos económicos con Ryanair desde España. Hospedaje muy accesible",
                 "🍋 Palermo o Catania, Sicilia (Italia): Playa linda y cultura"]

beach_economy_activities = ["🏕️ Dormir en carpa o hostel cerca de la playa",
                            "🤿 Hacer snorkel con sorbete (modo ratón)",
                            "🧺 Picnic al atardecer con vista al mar",
                            "🚶 Caminar por el paseo marítimo o calas escondidas",
                            "🏐 Juegos de playa (paletas, vóley, frisbee)"]

beach_luxury = ["💎 Maldivas: Vuelo largo, pero sigue siendo el top del lujo. A veces hay ofertas desde Madrid.",
                "🌺 Bora Bora, Polinesia Francesa: Muy lejos y carísimo. Pero... lugar soñado.",
                "🕶️ Ibiza o Formentera, España: Lujo europeo, yendo a los spots caros. Hoteles y beach clubs $$$.",
                "🇬🇷 Santorini o Mykonos, Grecia: Todo lujo blanco y celeste.",
                "🍋 Capri o Costa Amalfitana, Italia: Hoteles caros, mucha exclusividad y ferrys muy lindos",
                "🌴 Seychelles, África: Naturaleza y lujo en estado puro",
                "🌇 Dubái (The Palm): Lujo por todos lados, vuelos accesibles desde Europa.",
                "🚤 Niza, Mónaco, Saint-Tropez (Costa Azul): Full jet set europeo"]

beach_luxury_activities = ["🛥️ Paseo en yate privado",
                           "🍽️ Cena en restaurante Michelin frente al mar",
                           "💆 Masajes o spa en resort 5★",
                           "🌊 Deportes acuáticos con instructor (jetski, paddle VIP)",
                           "👨‍🍳 Clase de cocina gourmet frente al mar"]

beach_luxury_activities = ["🛥️ Paseo en yate privado",
                           "🍽️ Cena en restaurante Michelin frente al mar",
                           "💆 Masajes o spa en resort 5★",
                           "🌊 Deportes acuáticos con instructor (jetski, paddle VIP)",
                           "👨‍🍳 Clase de cocina gourmet frente al mar"]

mountain_economy = ["⛰️ Picos de Europa (España): Potes, Bulnes, Sotres: Naturaleza brutal y rutas increíbles.",
                    "🏞️ Pirineo Aragonés (España): Aínsa, Broto, Ordesa, camping y rutas gratuitas.",
                    "🥾 Valle de Benasque (España): Barato y con acceso al Aneto.",
                    "🏕️ Sierra de Gredos (España): Pueblitos, pozas y montaña sin gastar mucho.",
                    "🧗 Sierra de Guara (España): Ideal para barranquismo y rutas baratas.",
                    "🇵🇹 Serra da Estrela (Portugal): Poco turística y rural.",
                    "🇸🇰 Tatras (Eslovaquia/Polonia): Muy económico, caminatas brutales.",
                    "🇧🇬 Parque Nacional Rila o Pirin (Bulgaria): Glaciares y monasterios con poca gente."]

mountain_economy_activities = ["🥾 Trekking libre por rutas marcadas",
                               "🌌 Acampar bajo las estrellas",
                               "🏞️ Bañarse en ríos o lagos de montaña",
                               "📸 Hacer fotos de fauna y paisajes",
                               "🔥 Cocinar con anafe o fuego al aire libre"]

mountain_luxury = ["🏔️ Zermatt (Suiza): Lujo alpino y vistas al Matterhorn.",
                   "🇮🇹 Cortina d’Ampezzo (Italia): Paisajes imponentes y trekking top.",
                   "🇫🇷 Chamonix (Francia): Base del Mont Blanc, ideal para gourmets.",
                   "🌄 Andermatt (Suiza): Relax y excursiones nivel pro.",
                   "🎿 Lech (Austria): Aire puro y exclusividad alpina.",
                   "🌅 Lago de Como (Italia): Naturaleza con glamour.",
                   "🇪🇸 Baqueira y Valle de Arán (España): Rutas y pueblo con encanto.",
                   "🧖‍♀️ Cauterets y Gavarnie (Francia): Termas y hoteles boutique."]

mountain_luxury_activities = ["🥗 Senderismo guiado con picnic gourmet",
                              "♨️ Spa de montaña o baño termal exclusivo",
                              "🚁 Helicóptero panorámico",
                              "🍷 Cenas en refugios boutique con vino local",
                              "🧘‍♂️ Yoga al amanecer con vistas"]

city_economy = ["🇵🇹 Lisboa (Portugal): Precios razonables, vistas increíbles.",
                "🇵🇱 Cracovia (Polonia): Cultura, historia y buena onda.",
                "🇭🇺 Budapest (Hungría): Baños termales y castillos.",
                "🇧🇬 Sofía (Bulgaria): Historia ortodoxa y naturaleza cerca.",
                "🇪🇸 Valencia (España): Playa, cultura y más barata que otras.",
                "🏯 Granada (España): Tapas gratis, Alhambra y mezcla árabe.",
                "🇧🇦 Sarajevo (Bosnia): Historia fuerte y comida copada.",
                "🍕 Nápoles (Italia): Pizza top, auténtica y accesible."]

city_economy_activities = ["🚶 Free walking tours",
                           "🌮 Comer en mercados locales o food trucks",
                           "🖼️ Visitar museos gratis o con descuentos",
                           "🌇 Subir a miradores o parques con vistas",
                           "🚲 Moverse en bici o transporte público"]

city_luxury = ["🎨 París (Francia): Museos top y gastronomía de lujo.",
               "🏙️ Dubái (EAU): Rascacielos, 4x4 en el desierto, lujo extremo.",
               "🏞️ Zúrich (Suiza): Elegancia impecable y lago hermoso.",
               "👜 Milán (Italia): Moda, diseño y estilo.",
               "🧑‍🎨 Copenhague (Dinamarca): Moderna, estética y deliciosa.",
               "🎰 Mónaco: Casinos, Ferraris y glamour puro.",
               "🎭 Londres (UK): Cultural y con zonas exclusivas.",
               "🍸 Barcelona (España): Rooftops, estrellas Michelin y diseño."]

city_luxury_activities = ["🗺️ Tour privado con guía local",
                          "🍷 Cena en rooftops caros o restaurantes de moda",
                          "🛍️ Compras en boutiques de lujo",
                          "🏨 Hospedaje en hotel 5★ o palacio urbano",
                          "🎭 Obra de teatro, ballet o concierto exclusivo"]

# Duracion:
duración = ["📆 3 días", 
            "🌞 un mes", 
            "🧳 una semana", 
            "📌 un finde largo", 
            "🚫 TODAS tus vacaciones de trabajo", 
            "🏖️ 15 días"]

# Compañia:
compañía = ["🧍 nadie, vas solito",
            "🎉 un grupo de amigos",
            "👨‍👩‍👧‍👦 la familia",
            "💑 tu novia (si no tenés, vas solo pero tenés que conseguir una en el viaje)",
            "📱 la última persona que te envió un Whatsapp"]


# Presupuestos
budget_economy = ["💶 LLévate todo si no tenés un duro 😂", 
                  "🪙 Aproximadamente 500€", 
                  "💵 Yo llevaría unos 600€ por si las moscas"]

budget_luxury = ["🏦 Y tendrías que hipotecar la casa… chiste, son alrededor de 2000€", 
                 "💳 3.500€ y vale cada centavo", 
                 "👑 Mínimo 4000€, pero vas como un rey"]


import random

# Diccionario con destinos y confort
mapa_destinos = {
    ("playa", "economico"): (beach_economy, beach_economy_activities),
    ("playa", "lujo"): (beach_luxury, beach_luxury_activities),
    ("montaña", "economico"): (mountain_economy, mountain_economy_activities),
    ("montaña", "lujo"): (mountain_luxury, mountain_luxury_activities),
    ("ciudad", "economico"): (city_economy, city_economy_activities),
    ("ciudad", "lujo"): (city_luxury, city_luxury_activities)}

# Funcion
def vacation():

    preg1 = input("Quieres que tus vacaciones sean totalmente al azar🎲?(si o no): ")

    if preg1.strip().lower() == "si":
        clave = random.choice(list(mapa_destinos.keys()))
        destinos_posibles, actividades_posibles = mapa_destinos[clave]

        if clave[1] == "economico":
           presupuesto = random.choice(budget_economy)
        else:
            presupuesto = random.choice(budget_luxury)
            
        print("\n🧭 ¡Tu plan de vacaciones está listo! 🌍")
        print("────────────────────────────────────────")
        print(f"📍 Destino: {random.choice(destinos_posibles)}")
        print(f"🧑‍🤝‍🧑 Compañía: {random.choice(compañía)}")
        print(f"🗓️ Duración: {random.choice(duración)}")
        print(f"🎯 Actividad destacada: {random.choice(actividades_posibles)}")
        print(f"💰 Presupuesto estimado por persona: {presupuesto}")
        print("────────────────────────────────────────\n")

    elif preg1.strip().lower() == "no":
        preg2 = input("Vale, Quieres 🏖️ playa, 🏔️ montaña, o 🏙️ ciudad?: ")
        preg3 = input("Buena eleccion, Te vas en modo 🎒 economico o modo lujo💎?: ")
        preg4 = input("Cuanto tiempo quieres irte de vacaciones?: ")
        preg5 = input("Con quien/es te vas a ir?: ")
        clave = preg2.strip().lower(), preg3.strip().lower()

        if clave in mapa_destinos:
            destinos_posibles, actividades_posibles = mapa_destinos[clave]
            if preg3.strip().lower() == "lujo":
                presupuesto = random.choice(budget_luxury)
            else:
                presupuesto = random.choice(budget_economy)
            
            print("\n✏️ Plan personalizado generado:")
            print("────────────────────────────────────────")
            print(f"📍 Destino: {random.choice(destinos_posibles)}")
            print(f"🧑‍🤝‍🧑 Compañía: {preg5}")
            print(f"🗓️ Duración: {preg4}")
            print(f"🎯 Actividad destacada: {random.choice(actividades_posibles)}")
            print(f"💰 Presupuesto estimado por persona: {presupuesto}")
            print("────────────────────────────────────────\n")

        else:
            print("⚠️ Haz escrito mal el tipo de destino o confort")
    else:
        print("⚠️ Respuesta incorrecta")

while True:
    vacation()
    preg6 = input("🔚 ¿Deseas salir? (si para salir / no para seguir): ")
    if preg6.strip().lower() == "si":
        print("🚪 ¡Te fuiste de vacaciones ✈️ , nos vemos pronto! 😎")
        break
    elif preg6.strip().lower() == "no":
        continue
    else:
        print("⚠️ Respuesta incorrecta (responder si o no)")

