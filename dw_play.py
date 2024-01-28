from pytube import YouTube
import os
import shutil

os.system("clear")
print("⠀⠀\033[1;31m⢀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣄⣀⡀⠀⠀")
print("⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀")
print("⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀")
print("⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆")
print("⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇")
print("⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⢈⣹⣿⣿⣿⣿⣿⣿⣿⡇")
print("⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇")
print("⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇")
print("⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀")
print("⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀")
print("⠀⠀⠈⠉⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠉⠁⠀⠀")
print("")
print("  >>>>>*Dw_PlayYT*<<<<<")
print("")

carpeta = "YT_videos_descargados"
if not os.path.exists(carpeta):
    os.makedirs(carpeta)
else:
    print("")

# Función para descargar el video
def descargar_video(url):
    try:
        # Obtener objeto YouTube
        youtube = YouTube(url)

        # Obtener la mejor resolución disponible
        video = youtube.streams.get_highest_resolution()

        # Descargar el video
        video.download()
        print("")
        print("\033[1;31m[>]Descarga completada => \033[1;37m/YT_videos_descargados")
        # Mover el archivo descargado a la carpeta correspondiente
        nombre_archivo = video.default_filename
        shutil.move(nombre_archivo, os.path.join(carpeta, nombre_archivo))
    except Exception as e:
        print("\033[1;31m[>]Error al descargar el video:", str(e))

# URL del video
url = input("[>]Url: \033[1;37m")

# Llamar a la función para descargar el video
descargar_video(url)


