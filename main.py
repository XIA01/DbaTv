import flet as ft
import time
import random
from preguntas import preguntas_A, preguntas_B, preguntas_C
from flet import ScrollMode, ButtonStyle
from ficha import *

#from audio import audio_objects, play_audio, stop_audio
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#import os

# Obtén la ruta del archivo de credenciales desde la variable de entorno
#cred_path = os.environ.get("FIREBASE_CREDENTIALS")

# Inicializa Firebase Admin SDK con las credenciales
#cred = credentials.Certificate(cred_path)
# Obtiene una referencia a la colección "Top" en Firestore
#db = firestore.client()
#top_collection = db.collection('Top')
# Diccionario para almacenar los objetos de audio

def reiniciar_variables_globales():
    global puntuacion, batalla, mipj, batallaglobal, oponentes, preguntas_por_oponente, preguntas_respondidas, preguntas_seleccionadas, nombre, porcentajefinal
    
    # Restablecer todas las variables globales a sus valores iniciales
    puntuacion = []
    batalla = 0
    mipj = ""
    batallaglobal = 0
    oponentes = []
    preguntas_por_oponente = 8
    preguntas_respondidas = 0
    preguntas_seleccionadas = []
    nombre = ""
    porcentajefinal = 0.0

reiniciar_variables_globales()
def main(page: ft.Page):
    
    page.fonts = {
        "Light": r"\fonts\Exo2-Light.ttf",
        "Bold": r"\fonts\Exo2-Bold.ttf",
        "Thin": r"\fonts\Exo2-ThinItalic.ttf"
    }
        
    # Función para crear botones con valores mezclados
    def crear_botones_valores_aleatorios(opciones, preguntas, oponente):
        random.shuffle(opciones)  # Mezcla las opciones aleatoriamente
        botones = []
        for opcion in opciones:
            # Obtener el texto correspondiente a la opción
            texto_respuesta = obtener_texto_respuesta(opcion, preguntas, oponente)
            # Cada botón tiene un valor real y se asigna la función asignando al hacer clic
            botones.append(ft.ElevatedButton(str(texto_respuesta),style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=3),padding=10), on_click=lambda _, texto=str(opcion): asignando(texto, preguntas, oponente)))

        return botones
    
    # Función para obtener el texto de la respuesta
    def obtener_texto_respuesta(opcion, preguntas, oponente):
        # Acceder al texto correspondiente en función de la opción y el oponente
        texto_respuesta = preguntas[batalla]["respuestas_" + oponente]["boton" + str(opcion)]
        return texto_respuesta
    
    # Función para asignar puntuación y avanzar a la siguiente batalla
    def asignando(opcion, preguntas, enemy):
        global puntuacion
        #numero = int(opcion) 
        puntuacion.append(int(opcion))
        
        
       # if numero == 0:
       #     play_audio("abeeps0")
       # elif numero == 1:
       #     play_audio("abeeps1")
       # elif numero == 2:
        #    play_audio("abeeps2")
        vista_batalla(mipj, enemy, preguntas)
        
    # Función para calcular el porcentaje de puntaje obtenido
    def calcular_porcentaje_puntaje_obtenido(puntos_obtenidos, puntaje_maximo):
        if puntaje_maximo == 0:
            return 0
        porcentaje = (puntos_obtenidos / puntaje_maximo) * 100
        return porcentaje 
    # Función para obtener el mensaje según el porcentaje de puntaje obtenido
    def obtener_mensaje_porcentaje(porcentaje):
        for rango, mensaje in mensajes.items():
            if rango[0] <= porcentaje <= rango[1]:
                return mensaje
        return "Mmmmmmmmmmmmmm"
    
    # Vista resultados finales
    def mostrar_resultado_final():
        global porcentajefinal
        page.views.clear()
        
        suma_puntuacion = sum(puntuacion)
        porcentaje = calcular_porcentaje_puntaje_obtenido(suma_puntuacion, 28)
        porcentajefinal = round(porcentaje,2)
        mensaje = obtener_mensaje_porcentaje(porcentaje)
        
       # if porcentaje < 50:
       #     play_audio("fail")

       # elif 50 <= porcentaje <= 70:
            # Realiza una acción si el porcentaje está entre 50 y 70
       #     play_audio("mediumwim")

      #  else:
            # Realiza una acción si el porcentaje es mayor que 70
       #     play_audio("win")

        
        btn_siguiente = ft.ElevatedButton("Continuar a la tabla...", on_click=lambda _: vista_tabla())
        txt_puntuacion = ft.Text(f'Puntuacion: {suma_puntuacion}')
        imagen= ft.Image("\milei.jpeg",border_radius=90)
        imagen1= ft.Image("\mBullrich.jpg",border_radius=90)
        imagen2= ft.Image("\massa.jpg",border_radius=90)
        if mipj == "Milei":
            imagena= imagen
        elif mipj == "Bullrich":
            imagena= imagen1
        elif mipj == "Massa":
            imagena= imagen2
        tarjeta_pj = ft.Card(ft.Container(
            ft.Column([
                ft.Text(f"Tu candidato: {mipj}",font_family="Bold",size=17),
                imagena,
                ft.Column([
                    ft.ListTile(title=ft.Text("Afiliación Política",font_family="Bold"),
                            subtitle=ft.Text(candidatos[mipj]["Afiliación Política"],font_family="Light"),),
                    ft.ListTile(title=ft.Text("Plataforma Política",font_family="Bold"),
                            subtitle=ft.Text(candidatos[mipj]["Plataforma Política"],font_family="Light"),),
                    ft.ListTile(title=ft.Text("Enfoque de Campaña",font_family="Bold"),
                            subtitle=ft.Text(candidatos[mipj]["Enfoque de Campaña"],font_family="Light"),)
                ])
            
       ] ),padding=10))
        def items(count, puntuaciones):
            items = []
            for i in range(1, count + 1):
                pregunta = f"Pregunta {i}: {puntuaciones[i-1]} puntos"
                items.append(
                    ft.Container(
                        content=ft.Text(value=pregunta),
                        alignment=ft.alignment.center,
                        width=100,  # Ajusta el ancho según tus necesidades
                        height=25,
                        bgcolor=ft.colors.PINK_50,
                        border_radius=ft.border_radius.all(5),
                    )
                )
            return items
        # Divide las puntuaciones en dos listas
        puntuacion_parte1 = puntuacion[:7]  # Preguntas del 1 al 7
        puntuacion_parte2 = puntuacion[7:]  # Preguntas del 8 al 13
        row1 = ft.Row(spacing=5, controls=items(len(puntuacion_parte1), puntuacion_parte1),wrap=True)
        row2 = ft.Row(spacing=5, controls=items(len(puntuacion_parte2), puntuacion_parte2),wrap=True)       
        if oponentes[0] == "Milei":
            img_oponente1=imagen
        elif oponentes[0] == "Bullrich":
            img_oponente1=imagen1
        elif oponentes[0] == "Massa":
            img_oponente1=imagen2   
            
        tarjeta_oponente1 = ft.Card(ft.Container(
            ft.Column([
                ft.Text(f" Primer oponente: {oponentes[0]}",font_family="Bold",size=17),
                ft.Row([img_oponente1,ft.Column([ft.Text("Puntos obtenidos:",font_family="Light"),row1])],wrap=True)
            ]),padding=10)
        )
        if oponentes[1] == "Milei":
            img_oponente2=imagen
        elif oponentes[1] == "Bullrich":
            img_oponente2=imagen1
        elif oponentes[1] == "Massa":
            img_oponente2=imagen2   
            
        tarjeta_oponente2 = ft.Card(ft.Container(
            ft.Column([
                ft.Text(f" Segundo oponente: {oponentes[1]}",font_family="Bold",size=17),
                ft.Row([img_oponente2,ft.Column([ft.Text("Puntos obtenidos:",font_family="Light"),row2])],wrap=True)
            ]),padding=10)
        )
        
        tarjeta_mensaje = ft.Container(ft.Text(f"Haz acertado un {round(porcentaje, 2)}% por lo tanto... {mensaje}",font_family="Bold",size=22,text_align= ft.TextAlign.JUSTIFY,color=ft.colors.AMBER_50),border=ft.border.all(3, ft.colors.ON_PRIMARY),
                        gradient=ft.LinearGradient(
                                    begin=ft.alignment.top_center,
                                    end=ft.alignment.bottom_center,
                                colors=[ft.colors.ON_PRIMARY_CONTAINER, ft.colors.TEAL_ACCENT_700],
                                ),padding=ft.padding.all(20))
        
        
        
        
        
        
        pantalla_resultados = ft.View("/resultados",[
            ft.Column([ft.Text("RESULTADOS:",font_family="Bold",size=22,text_align= ft.TextAlign.CENTER),
                ft.Row(controls=[txt_puntuacion, btn_siguiente]),
                tarjeta_pj,
                tarjeta_oponente1,
                tarjeta_oponente2,
                tarjeta_mensaje
            ])
        ],scroll=ScrollMode.AUTO)
        
        page.views.append(pantalla_resultados)
        page.update()
    
    # Vista tabla de posiciones
    def vista_tabla():
        global nombre, mipj
        page.views.clear()
        #sonidos = [win, mediumwim, fail, abeeps1, abeeps2]
        #for sonido in sonidos:
        #    if sonido in page.overlay:
       #         page.overlay.remove(sonido)
        # Crear un TextField para que el usuario ingrese su nombre
        nombre_textfield = ft.TextField(label="Nombre",autofocus=True)
        
        # Obtener el valor ingresado por el usuario
        #nombre = nombre_textfield.value
        
        tabla = ft.View("/tabla", [ft.Text("Ingrese su nombre"), nombre_textfield, ft.ElevatedButton("Seguir", on_click=lambda _: vista_publicidad())],horizontal_alignment=ft.MainAxisAlignment.CENTER,vertical_alignment=ft.MainAxisAlignment.CENTER)
        
        
        page.views.append(tabla)
        page.update()
        '''
    def vista_top(nom):
        global nombre, mipj
        nombre = nom
        print(nombre)
        fecha_actual = datetime.now()
        # Crea un nuevo documento en la colección "Top" con los datos
        try:
        # Intenta agregar un documento
            top_collection.add({
                'Candidato': mipj,
                'Fecha de Registro': fecha_actual,
                'Nombre': nombre,
                'Porcentaje': int(porcentajefinal),
                'Puntuacion': sum(puntuacion)
            })
            print("Documento agregado con éxito.")
        except Exception as e:
            print(f"Error al agregar el documento: {e}")


        # Consulta la colección "Top" y ordena los resultados por puntuación y fecha de registro (en orden descendente)
        query = top_collection.order_by('Puntuacion', direction=firestore.Query.DESCENDING)

        

        # Obtiene los resultados de la consulta
        resultados = query.stream()

        # Limpia la vista actual
        page.views.clear()

        # Crea una vista para mostrar los datos ordenados en la tabla
        vista_tabla_top = []

        for resultado in resultados:
            data = resultado.to_dict()
            fecha_registro = data['Fecha de Registro'].strftime('%Y-%m-%d %H:%M:%S')
            nombre_jugador = data['Nombre']
            puntuacion_jugador = data['Puntuacion']
            porce = data['Porcentaje']
            candidat = data['Candidato']
            

            # Agrega los datos del jugador a la vista de tabla "Top"
            vista_tabla_top.append(ft.Text(f'Nombre: {nombre_jugador}',font_family="Light",color=ft.colors.YELLOW_50))
            vista_tabla_top.append(ft.Text(f'Puntuación: {puntuacion_jugador}({round(porce,2)}%)',font_family="Thin",color=ft.colors.YELLOW_50))
            vista_tabla_top.append(ft.Text(f'Candidato: {candidat}',font_family="Thin",color=ft.colors.YELLOW_50))
            vista_tabla_top.append(ft.Text(f'Fecha de Registro: {fecha_registro}',font_family="Thin",color=ft.colors.YELLOW_50))
            vista_tabla_top.append(ft.Divider())
            
            
            

        # Crea una vista que muestra la tabla "Top"
        btn_seguir = ft.ElevatedButton("Continuar", on_click=lambda _: vista_publicidad())
        tabla_top = ft.View("/tabla_top", [ft.Text("Tabla de Posiciones",font_family="Bold",color=ft.colors.YELLOW), btn_seguir, *vista_tabla_top],scroll = ScrollMode.ALWAYS,bgcolor=ft.colors.ON_SECONDARY_CONTAINER
)

        # Agrega la vista de la tabla "Top" a la página
        page.views.append(tabla_top)
        page.update()



        '''

    # Vista publicidad
    def vista_publicidad():
        page.views.clear()
        # Crear un TextSpan con un enlace que se abrirá en una nueva ventana (_blank)
        enlace_span = ft.Text(
            spans=[ft.TextSpan(
            text="Enlace a Tecito",
            url="https://tecito.app/sentineldev",
            url_target="_blank",
            style=ft.TextStyle(size=20,shadow=ft.BoxShadow.blur_radius,color=ft.colors.ON_PRIMARY)
        )])
        # Crear un Text con el TextSpan
        textofinal = "¡Felicidades por completar mi primer proyecto con Flet, DbaT: ¡Pon a Prueba tu Militancia! Como estudiante y apasionado de la programación en Python, estoy en constante aprendizaje y crecimiento, y tu generosidad podría marcar una diferencia significativa en mi viaje educativo. Tu apoyo financiero es esencial para respaldar mis estudios y proyectos educativos. Cada donación, sin importar su tamaño, impulsa mis esfuerzos y me permite seguir explorando y compartiendo conocimiento. Te invito a donar y hacer una diferencia hoy mismo. Si deseas brindar apoyo a mi primer proyecto y dejarme un tecito para recargar energías mientras sigo aprendiendo y creciendo en el mundo de la programación, sería muy apreciado. Además, si deseas participar nuevamente o probar tu suerte con otro candidato, simplemente presiona el botón 'Volver al menú'. Tu contribución es apreciada y valiosa.¡Gracias por tu generosidad y apoyo en este emocionante viaje de aprendizaje!"
        
        textomedio = "¡Gran trabajo en el primer debate! Ahora es el momento de enfrentarte a tu próximo oponente. Prepárate para continuar defendiendo tus propuestas y demostrar por qué eres el candidato presidencial ideal. ¡Sigamos con el siguiente desafío!"
        if batallaglobal < len(oponentes):
            # Quedan oponentes, muestra el botón "Comenzar nueva ronda"
            tabla = ft.View("/publicidad", [ft.Container(
                ft.Column([
                ft.Text(textomedio, font_family="Light",color=ft.colors.BROWN_50),
                ft.Text(f"{mipj} ¿Estas listo?",color=ft.colors.BROWN_50),
                ft.ElevatedButton("Comenzar nueva ronda", on_click=lambda _: comenzar_nueva_ronda())
                ],alignment=ft.MainAxisAlignment.CENTER)
            ,padding=10,alignment=ft.alignment.center)],bgcolor= ft.colors.ON_SECONDARY_CONTAINER,vertical_alignment= ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.MainAxisAlignment.CENTER,scroll=ft.ScrollMode.ALWAYS
                                            )
                                            
        else:
            # No quedan oponentes, muestra el botón "Volver al menú"
            tabla = ft.View("/publicidad", [
                ft.Container(ft.Text(textofinal,font_family="Light",text_align=ft.TextAlign.JUSTIFY,color=ft.colors.GREY_50),border=ft.border.all(3, ft.colors.ON_PRIMARY),
                        gradient=ft.LinearGradient(
                                    begin=ft.alignment.top_center,
                                    end=ft.alignment.bottom_center,
                                colors=[ft.colors.ON_PRIMARY_CONTAINER, ft.colors.TEAL_ACCENT_700],
                                ),padding=ft.padding.all(20)),
                
                ft.Text(f"{nombre} Gracias por jugar!",font_family="Thin",color=ft.colors.ON_SECONDARY,size=24),
                enlace_span,
                ft.ElevatedButton("Volver al menú", on_click=lambda _: [vista_menu(), reiniciar_variables_globales()])

            ],vertical_alignment= ft.MainAxisAlignment.CENTER,bgcolor= ft.colors.ON_SECONDARY_CONTAINER, horizontal_alignment=ft.MainAxisAlignment.CENTER,scroll=ft.ScrollMode.ALWAYS)
        page.views.append(tabla)
        page.update()
        
    def comenzar_nueva_ronda():
        global batalla, preguntas_respondidas, preguntas_por_oponente

        # Reinicia las variables necesarias para una nueva ronda
        batalla = 0
        preguntas_respondidas = 0
        
        # Verifica si se han agotado todos los oponentes
        if batallaglobal == len(oponentes):
            mostrar_resultado_final()
        else:
            # Obtiene el siguiente oponente
            siguiente_oponente = oponentes[batallaglobal]

            # Realiza cualquier otra lógica que necesites aquí

            # Llama a la función para mostrar la vista de batalla con el nuevo oponente
            vista_batalla(mipj, siguiente_oponente, preguntas_seleccionadas)
   
    # Función para cambiar de personaje
    def cambio(event, candidato):
      #  sonidos = [aintro, abatalla, abeeps0, abeeps1, abeeps2]
       # for sonido in sonidos:
      ##          page.overlay.remove(sonido)
      #  page.overlay.append(abatalla)
       # stop_audio("aintro")
        page.views.clear()
       # play_audio("abatalla")
        page.views.append(vista_elegido(candidato))
        
        page.update()
    
    # Imagen de menú
    imagen_menu = ft.Container(ft.Image(
        src= f"\inicio.jpeg",
        width=300
        #height=300
         ),
                        border_radius=10,
                        border=ft.border.all(7, ft.colors.WHITE),
                        alignment= ft.alignment.top_center,
                        margin=5,
                        width=300,
                        height=300
                        )
    
    estilobtn= ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),color=ft.colors.ON_SECONDARY_CONTAINER,bgcolor=ft.colors.INDIGO_100)
    card_bullrich = ft.Card(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(src=f"\mBullrich.jpg",border_radius=90),
                    ft.Column([ft.Text("Bullrich",color=ft.colors.BLACK,weight=ft.FontWeight.W_900),ft.Text("Centro Izquierda",color=ft.colors.BLACK,weight=ft.FontWeight.W_400,size=10),ft.ElevatedButton(text="Elegir",style=estilobtn, on_click=lambda _: cambio(_, "Bullrich"))])
                ]
            )
        ,padding=5)
    ,color=ft.colors.BLUE_100,margin=10)
    card_milei = ft.Card(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(src= f"\milei.jpeg",border_radius=90),
                    ft.Column([ft.Text("Milei",color=ft.colors.BLACK,weight=ft.FontWeight.W_900),ft.Text("Liberal",color=ft.colors.BLACK,weight=ft.FontWeight.W_400,size=10),ft.ElevatedButton(text="Elegir",style=estilobtn, on_click=lambda _: cambio(_, "Milei"))])
                ]
            )
        ,padding=5)
    ,color=ft.colors.BLUE_100,margin=10)
    card_massa = ft.Card(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(src= f"\massa.jpg",border_radius=90),
                    ft.Column([ft.Text("Massa",color=ft.colors.BLACK,weight=ft.FontWeight.W_900),ft.Text("Izquierda Conservadora",color=ft.colors.BLACK,weight=ft.FontWeight.W_400,size=10),ft.ElevatedButton(text="Elegir",style=estilobtn, on_click=lambda _: cambio(_, "Massa"))])
                ]
            )
        ,padding=5)
    ,color=ft.colors.BLUE_100,margin=10)
    
    frase = ft.Container(ft.Text("Bienvenido a DbaT: ¡Pon a Prueba tu Militancia! Elige a tu candidato y prepárate para una intensa batalla de argumentos políticos. ¿Quién ganará el debate? ¡Tú decides!", font_family="Light",size=15,color=ft.colors.AMBER_50)
                         ,border=ft.border.all(3, ft.colors.ON_PRIMARY),
                        gradient=ft.LinearGradient(
                                    begin=ft.alignment.top_center,
                                    end=ft.alignment.bottom_center,
                                colors=[ft.colors.ON_PRIMARY_CONTAINER, ft.colors.TERTIARY],
                                ),padding=ft.padding.all(10)
                        )
    btn_milei = card_milei
    btn_massa = card_massa
    btn_bullrich = card_bullrich
    #Intro de la aplicacion
    intro = ft.Container(ft.Image(
        src= f"\intro1.gif",
        width=300,
        height=300,
        fit=ft.ImageFit.CONTAIN,expand=True),
                        border_radius=10,
                        margin= ft.margin.all(10),
                        alignment=ft.alignment.center)
        
    
    # Vista elegido
    def vista_elegido(candi :str):
        global oponentes, preguntas_respondidas, batallaglobal, preguntas_seleccionadas, mipj
        # Genera los dos oponentes y reinicia los contadores
        oponentes = generar_oponentes(candi)
        preguntas_respondidas = 0
        batallaglobal = 0
        mipj = candi
        
        if candi == "Milei":
            preguntas_seleccionadas = seleccionar_preguntas_aleatorias(preguntas_A)
        elif candi == "Massa":
            preguntas_seleccionadas = seleccionar_preguntas_aleatorias(preguntas_B)
        elif candi == "Bullrich":
            preguntas_seleccionadas = seleccionar_preguntas_aleatorias(preguntas_C) 
         
        txt_vista = ft.View("/ready",[ft.Image("\menu.jpeg",width=400,border_radius=10),
           ft.Container( ft.Text(f'¡Prepárate para el Desafío Presidencial 2023! En este juego, asumirás el rol de {candi} tu candidato presidencial y te enfrentarás a dos oponentes en un debate político. Ahora mismo enfrentaras a {oponentes[batallaglobal]} y luego a {oponentes[batallaglobal+1]}.Deberás responder siete preguntas sobre tus propias propuestas de campaña. Cada respuesta correcta sumará 2 puntos para "Muy correcto", 1 para "Correcto" y 0 para "Mal". ¡Demuestra tus conocimientos y habilidades para llegar a un máximo de 28 puntos y conviértete en un candidato presidencial exitoso en este emocionante debate!',weight=ft.FontWeight.W_700,font_family="Light",color=ft.colors.AMBER_50),               border=ft.border.all(3, ft.colors.ON_PRIMARY),
                                      gradient=ft.LinearGradient(
                                    begin=ft.alignment.top_center,
                                    end=ft.alignment.bottom_center,
                                       colors=[ft.colors.ON_PRIMARY_CONTAINER, ft.colors.TERTIARY],
                                      ),padding=ft.padding.all(10)),
            ft.ElevatedButton("Estoy listo!", on_click=lambda _: vista_batalla(candi, oponentes[batallaglobal], preguntas_seleccionadas))
            ],vertical_alignment= ft.MainAxisAlignment.CENTER, scroll=ScrollMode.ALWAYS,bgcolor=ft.colors.ON_SECONDARY_CONTAINER
            )
        return txt_vista
    
    # Función para gestionar la vista de la batalla
    def vista_batalla(player, enemy, preguntas):
        global batalla, preguntas_respondidas, batallaglobal
        # Verificar si abatalla está en la lista overlay antes de intentar eliminarlo
        #if abatalla in page.overlay:
         #   page.overlay.remove(abatalla)
       
        page.views.clear()

        if batalla < preguntas_por_oponente:
            pregunta_actual = preguntas[batalla]["texto"]
             # Verificar cuál es el oponente actual en función del contador global
            enemy = oponentes[batallaglobal]
            if enemy == "Massa":
                refute_oponente = preguntas[batalla]["respuestas_Massa"]["refute"]
            elif enemy == "Bullrich":
                refute_oponente = preguntas[batalla]["respuestas_Bullrich"]["refute"]
            else:
                refute_oponente = preguntas[batalla]["respuestas_Milei"]["refute"]

            opciones_respuesta = [0, 1, 2]
            botones_aleatorios = crear_botones_valores_aleatorios(opciones_respuesta, preguntas, enemy)

            page.views.append(ft.View("/batalla", [
                ft.Column([
                    ft.Text(f"Señor {player} la pregunta es: {pregunta_actual}",size=20,font_family="Bold"),ft.Text(f'{enemy} dice: {refute_oponente}',size=17,font_family="Light"),
                    ft.Text(f"¿Cuál es su respuesta {player}?",size=22,font_family="Thin")
                ] + botones_aleatorios)
            ],scroll=ft.ScrollMode.ALWAYS))
            
            page.update()
            
            batalla += 1
            preguntas_respondidas += 1

        # Si se han respondido todas las preguntas con el oponente actual, cambia de oponente
        if preguntas_respondidas == preguntas_por_oponente:
            preguntas_respondidas = 0
            batallaglobal += 1
            batalla = 0  # Reinicia el contador de batallas
            
            # Verifica si se han agotado todos los oponentes
            if batallaglobal == len(oponentes):
                mostrar_resultado_final()
            else:
                # Llama a la vista de publicidad antes de comenzar la siguiente ronda
                vista_publicidad()
        
    # Función para gestionar la vista del menú principal
    def vista_menu():
        global batalla, puntuacion
        batalla = 0
        puntuacion = []  # Reiniciar puntuación al volver al menú
        #play_audio("aintro")
        page.views.clear()
        page.views.append(ft.View("/menu",[imagen_menu, frase,ft.Row([btn_milei, btn_massa, btn_bullrich],wrap=True)],scroll = ScrollMode.ALWAYS, bgcolor=ft.colors.ON_SECONDARY_CONTAINER))
        page.update()
    
    # Función para generar oponentes
    def generar_oponentes(personaje_principal):
        personajes_disponibles = ["Milei", "Massa", "Bullrich"]

        # Remover el personaje principal de la lista de disponibles
        personajes_disponibles.remove(personaje_principal)

         # Elegir aleatoriamente dos oponentes de los personajes restantes
        oponentes_aleatorios = random.sample(personajes_disponibles, 2)

        return oponentes_aleatorios
    
    # Función para seleccionar preguntas aleatorias
    def seleccionar_preguntas_aleatorias(diccionario_preguntas):
        # Obtener las claves de todas las preguntas disponibles
        claves_preguntas = list(diccionario_preguntas.keys())
    
        # Verificar que haya al menos 7 preguntas disponibles
        if len(claves_preguntas) < 7:
            raise ValueError("El diccionario de preguntas debe contener al menos 7 preguntas.")

        # Elegir aleatoriamente 8 claves de preguntas únicas (aumentar a 8 para mostrar 8 preguntas)
        claves_seleccionadas = random.sample(claves_preguntas, 8)

        # Crear una lista con las preguntas seleccionadas
        preguntas_seleccionadas = [diccionario_preguntas[clave] for clave in claves_seleccionadas]

        return preguntas_seleccionadas

    # Agregar el texto de introducción y pasar al menú principal después de un retraso
   # page.overlay.append(aintro)
   # Agrega los objetos de audio al overlay de la página
    
    page.controls.append(intro)
    page.bgcolor = ft.colors.ON_SECONDARY_CONTAINER
    #page.overlay.extend(audio_objects.values())
    
    page.update()
    time.sleep(3)
    vista_menu()
    
# Iniciar la aplicación Flet con dos carpetas de activos
ft.app(target=main, assets_dir="assets/")

