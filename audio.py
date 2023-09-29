# audio.py

import flet as ft

# Define tus objetos de audio
audio_objects = {
    "aintro": ft.Audio(src=r"\audio\intro.mp3", autoplay=False),
    "abatalla": ft.Audio(src=r"\audio\batalla.mp3", autoplay=False),
    "abeeps0": ft.Audio(src=r"\audio\beeps0.mp3", autoplay=False),
    "abeeps1": ft.Audio(src=r"\audio\beeps1.mp3", autoplay=False),
    "abeeps2": ft.Audio(src=r"\audio\beeps2.mp3", autoplay=False),
    "win": ft.Audio(src=r"\audio\win.mp3", autoplay=False),
    "mediumwim": ft.Audio(src=r"\audio\mediumwim.mp3", autoplay=False),
    "fail": ft.Audio(src=r"\audio\fail.mp3", autoplay=False)
}

# Función para reproducir un objeto de audio por su nombre
def play_audio(audio_name):
    if audio_name in audio_objects:
        audio = audio_objects[audio_name]
        audio.play()

# Función para detener un objeto de audio por su nombre
def stop_audio(audio_name):
    if audio_name in audio_objects:
        audio = audio_objects[audio_name]
        audio.pause()
        audio.seek(0)
