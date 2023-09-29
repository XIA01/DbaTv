import flet as ft

candidatos = {
    "Milei": {
        "Nombre": "Javier Milei",
        "Afiliación Política": "Liberal",
        "Plataforma Política": "Defensor del liberalismo económico, promueve la reducción del tamaño del Estado, menos regulaciones y más libertad económica. Favorable a políticas de mercado libre y reducción de impuestos.",
        "Enfoque de Campaña": "Destacará la importancia de la libertad individual, la propiedad privada y la iniciativa empresarial como motores del crecimiento económico y la prosperidad."
    },
    "Massa": {
        "Nombre": "Sergio Massa",
        "Afiliación Política": "Izquierda Conservadora",
        "Plataforma Política": "Aboga por políticas sociales más amplias y una mayor intervención del Estado en la economía. Promueve la igualdad de ingresos y el acceso equitativo a los servicios públicos.",
        "Enfoque de Campaña": "Resaltará la importancia de la justicia social, la redistribución de la riqueza y la protección de los derechos laborales y sociales."
    },
    "Bullrich": {
        "Nombre": "Patricia Bullrich",
        "Afiliación Política": "Centro Izquierda",
        "Plataforma Política": "Busca un equilibrio entre políticas económicas libres y un fuerte compromiso con la inclusión social. Promueve la inversión en infraestructura y la modernización del Estado.",
        "Enfoque de Campaña": "Destacará su enfoque pragmático y su compromiso con la construcción de un país equitativo y competitivo."
    }
}
# Acceder al nombre del candidato "Milei"
nombre_milei = candidatos["Milei"]["Nombre"]
#print("Nombre de Milei:", nombre_milei)

# Acceder a la afiliación política de "Milei"
afiliacion_milei = candidatos["Milei"]["Afiliación Política"]
#print("Afiliación Política de Milei:", afiliacion_milei)

# Acceder a la plataforma política de "Milei"
plataforma_milei = candidatos["Milei"]["Plataforma Política"]
#print("Plataforma Política de Milei:", plataforma_milei)

# Acceder al enfoque de campaña de "Milei"
enfoque_milei = candidatos["Milei"]["Enfoque de Campaña"]
#print("Enfoque de Campaña de Milei:", enfoque_milei)

# Acceder al nombre del candidato "Massa"
nombre_massa = candidatos["Massa"]["Nombre"]

# Acceder a la afiliación política de "Massa"
afiliacion_massa = candidatos["Massa"]["Afiliación Política"]

# Acceder a la plataforma política de "Massa"
plataforma_massa = candidatos["Massa"]["Plataforma Política"]

# Acceder al enfoque de campaña de "Massa"
enfoque_massa = candidatos["Massa"]["Enfoque de Campaña"]

# Acceder al nombre del candidato "Bullrich"
nombre_bullrich = candidatos["Bullrich"]["Nombre"]

# Acceder a la afiliación política de "Bullrich"
afiliacion_bullrich = candidatos["Bullrich"]["Afiliación Política"]

# Acceder a la plataforma política de "Bullrich"
plataforma_bullrich = candidatos["Bullrich"]["Plataforma Política"]

# Acceder al enfoque de campaña de "Bullrich"
enfoque_bullrich = candidatos["Bullrich"]["Enfoque de Campaña"]

#SONIDOS
'''
aintro = ft.Audio(
        src="/audio/intro.mp3", autoplay=True
    )
abatalla = ft.Audio(
        src="/audio/batalla.mp3", autoplay=True
    )
abeeps0 = ft.Audio(
        src="/audio/beeps0.mp3", autoplay=True
    )
abeeps1 = ft.Audio(
        src="/audio/beeps1.mp3", autoplay=True
    )
abeeps2 = ft.Audio(
        src="/audio/beeps2.mp3", autoplay=True
    )

win = ft.Audio(
        src="/audio/win.mp3", autoplay=True
    )
mediumwim = ft.Audio(
        src="/audio/mediumwim.mp3", autoplay=True
    )
fail = ft.Audio(
        src="/audio/fail.mp3", autoplay=True
    )
'''
# Diccionario de mensajes para diferentes rangos de porcentaje de aciertos
mensajes = {
    (0, 5): "¡Necesitas mejorar tu conocimiento sobre el candidato y sus propuestas! La conciencia cívica es fundamental para tomar decisiones informadas.",
    (6, 10): "Tienes un conocimiento muy limitado. ¡Investiga más sobre el candidato y sus políticas para ser un ciudadano informado!",
    (11, 15): "Tu conocimiento es insuficiente. La democracia se basa en ciudadanos bien informados. Dedica tiempo a aprender sobre el candidato y sus propuestas.",
    (16, 20): "Todavía tienes mucho por aprender. ¡La participación cívica es esencial en una sociedad democrática!",
    (21, 25): "Tienes un conocimiento básico, pero aún hay espacio para crecer. Sigue investigando y sigue de cerca las elecciones.",
    (26, 30): "Estás en el camino correcto, pero debes profundizar en tus conocimientos para tomar decisiones informadas en las elecciones.",
    (31, 35): "Tu conocimiento es decente, pero puedes hacerlo mejor. No te conformes, sigue informándote sobre el candidato y sus políticas.",
    (36, 40): "Tienes un conocimiento sólido, ¡sigue así! La conciencia cívica es clave para el funcionamiento de la democracia.",
    (41, 45): "¡Muy bien! Tienes un buen dominio del tema y estás en camino de tomar decisiones informadas en las elecciones.",
    (46, 50): "¡Excelente! Tu conocimiento es impresionante y tu conciencia cívica es admirable.",
    (51, 55): "Eres un ciudadano ejemplar con un conocimiento destacado sobre el candidato y sus propuestas. ¡Sigue participando activamente!",
    (56, 60): "¡Impresionante! Tu compromiso con la conciencia cívica es extraordinario. Continúa siendo un modelo a seguir en tu comunidad.",
    (61, 65): "Tienes un conocimiento sólido y un fuerte compromiso cívico. Continúa defendiendo la democracia y construyendo una patria más grande.",
    (66, 70): "¡Tu conocimiento es impresionante! Sigues demostrando un profundo amor por tu país. Juntos, podemos hacer una patria más grande y justa.",
    (71, 75): "Eres un ciudadano ejemplar con un conocimiento destacado. Tu contribución a una patria más grande no pasa desapercibida.",
    (76, 80): "Tu compromiso con la conciencia cívica es extraordinario. Sigues construyendo una patria más fuerte y solidaria para todos.",
    (81, 85): "Eres un verdadero patriota. Tu conocimiento y tu amor por el país son admirables. Juntos, podemos lograr una patria más grande y próspera.",
    (86, 90): "Tu dedicación a la construcción de una patria más grande es inspiradora. Tu ejemplo motiva a otros a unirse a la causa.",
    (91, 95): "¡Eres un líder cívico excepcional! Tu compromiso con la patria es un faro de esperanza para todos. Sigamos trabajando juntos por un país más grande.",
    (96, 100): "¡Eres un verdadero héroe cívico! Tu conocimiento, compromiso y pasión por una patria más grande son un regalo para nuestra nación. ¡Gracias por tu servicio!",
}


