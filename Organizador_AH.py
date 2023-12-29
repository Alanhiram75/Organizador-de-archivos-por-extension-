# Librerías
import os
import glob
import shutil
import time

# Comprueba y crea carpetas
while True:
    if not os.path.exists("documentos"):
        os.mkdir("documentos")
    if not os.path.exists("fotos"):
        os.mkdir("fotos")
    if not os.path.exists("videos"):
        os.mkdir("videos")
    if not os.path.exists("audios"):
        os.mkdir("audios")
    if not os.path.exists("ejecutables"):
        os.mkdir("ejecutables")
    if not os.path.exists("otros"):
        os.mkdir("otros")

    # Variables de extensiones de archivo
    #v imagenes
    png = glob.glob("*.png")
    jpg = glob.glob("*.jpg")
    #v videos
    mp4 = glob.glob("*.mp4")
    mkv = glob.glob("*.mkv")
    avi = glob.glob("*.avi")
    #v audio
    mp3 = glob.glob("*.mp3")
    #v documentos
    pdf = glob.glob("*.pdf")
    doc = glob.glob("*.doc")
    exel = glob.glob("*.xlsx")
    word = glob.glob("*.docx")
    #v ejecutable
    exe = glob.glob("*.exe")
    #v otros
    zip_files = glob.glob("*.zip")
    rar = glob.glob("*.rar")

    # Mover archivos a carpetas correspondientes
    for archivo in png + jpg:
        shutil.move(archivo, "fotos")

    for archivo in mp4 + mkv + avi:
        shutil.move(archivo, "videos")

    for archivo in mp3:
        shutil.move(archivo, "audios")

    for archivo in pdf + doc + exel + word:
        shutil.move(archivo, "documentos")

    for archivo in exe:
        shutil.move(archivo, "ejecutables")

    for archivo in zip_files + rar:
        shutil.move(archivo, "otros")

    #pequeño retraso antes de volver a comprobar
    time.sleep(60)# Puedes ajustar el tiempo según tus necesidades
    
    #autor:Alan Hiram Alvarez Bazan