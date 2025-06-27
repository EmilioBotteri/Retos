

import streamlit as st
import random

# Datos de vacaciones

# Destinos y actividades
mapa_destinos = {
    ("playa", "economico"): ([
        "🏖️ Algarve, Portugal: Barato para llegar, comida y hospedaje accesibles",
        "🌅 Costa Brava, España: Muy lindo poco gasto en transporte",
        "🏝️ Islas Canarias (Tenerife, Lanzarote, Gran Canaria): Vuelos low cost desde península",
        "☀️ Malta: Chiquito, fácil de recorrer, buen clima casi todo el año y vuelos baratos",
        "🌊 Kotor, Montenegro: Playas tranquilas, barato comer y dormir",
        "🇭🇷 Zadar o Split, Croacia: Se consiguen vuelos barato si sacás con tiempo",
        "🌴 Marrakech + Essaouira, Marruecos: Vuelos económicos con Ryanair desde España. Hospedaje muy accesible",
        "🍋 Palermo o Catania, Sicilia (Italia): Playa linda y cultura"
    ], [
        "🏕️ Dormir en carpa o hostel cerca de la playa",
        "🤿 Hacer snorkel con sorbete (modo ratón)",
        "🧺 Picnic al atardecer con vista al mar",
        "🚶 Caminar por el paseo marítimo o calas escondidas",
        "🏐 Juegos de playa (paletas, vóley, frisbee)"
    ]),

    ("playa", "lujo"): ([
        "💎 Maldivas: Vuelo largo, pero sigue siendo el top del lujo",
        "🌺 Bora Bora, Polinesia Francesa: Muy lejos y carísimo",
        "🕶️ Ibiza o Formentera, España: Lujo europeo, beach clubs $$$",
        "🇬🇷 Santorini o Mykonos, Grecia: Todo lujo blanco y celeste",
        "🍋 Capri o Costa Amalfitana, Italia: Hoteles caros y exclusivos",
        "🌴 Seychelles, África: Naturaleza y lujo",
        "🌇 Dubái (The Palm): Lujo por todos lados",
        "🚤 Niza, Mónaco, Saint-Tropez: Jet set europeo"
    ], [
        "🛥️ Paseo en yate privado",
        "🍽️ Cena en restaurante Michelin",
        "💆 Masajes en resort 5★",
        "🌊 Deportes acuáticos VIP",
        "👨‍🍳 Clase de cocina gourmet"
    ]),

    ("montaña", "economico"): ([
        "⛰️ Picos de Europa (España)",
        "🏞️ Pirineo Aragonés (España)",
        "🥾 Valle de Benasque (España)",
        "🏕️ Sierra de Gredos (España)",
        "🧗 Sierra de Guara (España)",
        "🇵🇹 Serra da Estrela (Portugal)",
        "🇸🇰 Tatras (Eslovaquia/Polonia)",
        "🇧🇬 Parque Nacional Rila o Pirin (Bulgaria)"
    ], [
        "🥾 Trekking libre",
        "🌌 Acampar bajo las estrellas",
        "🏞️ Bañarse en ríos o lagos",
        "📸 Hacer fotos de paisajes",
        "🔥 Cocinar al aire libre"
    ]),

    ("montaña", "lujo"): ([
        "🏔️ Zermatt (Suiza)",
        "🇮🇹 Cortina d’Ampezzo (Italia)",
        "🇫🇷 Chamonix (Francia)",
        "🌄 Andermatt (Suiza)",
        "🎿 Lech (Austria)",
        "🌅 Lago de Como (Italia)",
        "🇪🇸 Baqueira y Valle de Arán (España)",
        "🧖‍♀️ Cauterets y Gavarnie (Francia)"
    ], [
        "🥗 Senderismo con picnic gourmet",
        "♨️ Spa o termas exclusivas",
        "🚁 Helicóptero panorámico",
        "🍷 Cena en refugio boutique",
        "🧘‍♂️ Yoga con vistas"
    ]),

    ("ciudad", "economico"): ([
        "🇵🇹 Lisboa (Portugal)",
        "🇵🇱 Cracovia (Polonia)",
        "🇭🇺 Budapest (Hungría)",
        "🇧🇬 Sofía (Bulgaria)",
        "🇪🇸 Valencia (España)",
        "🏯 Granada (España)",
        "🇧🇦 Sarajevo (Bosnia)",
        "🍕 Nápoles (Italia)"
    ], [
        "🚶 Free walking tours",
        "🌮 Comer en mercados locales",
        "🖼️ Museos gratis o con descuento",
        "🌇 Miradores y parques",
        "🚲 Bici o transporte público"
    ]),

    ("ciudad", "lujo"): ([
        "🎨 París (Francia)",
        "🏙️ Dubái (EAU)",
        "🏞️ Zúrich (Suiza)",
        "👜 Milán (Italia)",
        "🧑‍🎨 Copenhague (Dinamarca)",
        "🎰 Mónaco",
        "🎭 Londres (UK)",
        "🍸 Barcelona (España)"
    ], [
        "🗺️ Tour privado con guía",
        "🍷 Cena en rooftops caros",
        "🛍️ Compras de lujo",
        "🏨 Hotel 5★ o palacio urbano",
        "🎭 Obra de teatro o concierto"
    ])
}

compañía = [
    "🧍 nadie, vas solito",
    "🎉 un grupo de amigos",
    "👨‍👩‍👧‍👦 la familia",
    "💑 tu novia (o conseguir una en el viaje)",
    "📱 la última persona que te envió un WhatsApp"
]

duración = [
    "📆 3 días",
    "🌞 un mes",
    "🧳 una semana",
    "📌 un finde largo",
    "🚫 TODAS tus vacaciones de trabajo",
    "🏖️ 15 días"
]

budget_economy = [
    "💶 LLévate todo si no tenés un duro 😂",
    "🪙 Aproximadamente 500€",
    "💵 Yo llevaría unos 600€ por si las moscas"
]

budget_luxury = [
    "🏦 Tendrías que hipotecar la casa… chiste, 2000€",
    "💳 3.500€ y vale cada centavo",
    "👑 Mínimo 4000€, pero vas como un rey"
]

# Streamlit App
st.set_page_config(page_title="Generador de Vacaciones", page_icon="🌴")
st.title("🌴 Generador de Vacaciones")
st.write("¡Planificá tus vacaciones con estilo y en segundos!")

modo = st.radio("¿Querés que sea aleatorio o personalizado?", ["🎲 Azar total", "🛠️ Personalizado"])

if modo == "🎲 Azar total":
    clave = random.choice(list(mapa_destinos.keys()))
    destinos, actividades = mapa_destinos[clave]
    presu = random.choice(budget_luxury if clave[1] == "lujo" else budget_economy)

    st.subheader("🧭 ¡Tu plan de vacaciones!")
    st.markdown(f"📍 **Destino:** {random.choice(destinos)}")
    st.markdown(f"🧑‍🤝‍🧑 **Compañía:** {random.choice(compañía)}")
    st.markdown(f"🗓️ **Duración:** {random.choice(duración)}")
    st.markdown(f"🎯 **Actividad destacada:** {random.choice(actividades)}")
    st.markdown(f"💰 **Presupuesto estimado por persona:** {presu}")

else:
    tipo = st.selectbox("¿Playa, montaña o ciudad?", ["playa", "montaña", "ciudad"])
    nivel = st.selectbox("¿Modo económico o de lujo?", ["economico", "lujo"])
    clave = (tipo, nivel)

    if clave in mapa_destinos:
        destinos, actividades = mapa_destinos[clave]
        compania = st.selectbox("¿Con quién vas?", compañía)
        dur = st.selectbox("¿Cuánto tiempo?", duración)
        presu = random.choice(budget_luxury if nivel == "lujo" else budget_economy)

        st.subheader("✏️ Tu plan personalizado")
        st.markdown(f"📍 **Destino:** {random.choice(destinos)}")
        st.markdown(f"🧑‍🤝‍🧑 **Compañía:** {compania}")
        st.markdown(f"🗓️ **Duración:** {dur}")
        st.markdown(f"🎯 **Actividad destacada:** {random.choice(actividades)}")
        st.markdown(f"💰 **Presupuesto estimado por persona:** {presu}")
    else:
        st.error("Combinación no válida. Verificá las opciones.")


# CODIGO PARA CORRERLO EN LA WEB
# streamlit run Modulos\Retos\reto_vacaciones_streamlit_web.py 