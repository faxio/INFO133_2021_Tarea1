import collections
import os
from typing import Collection
from pymongo import MongoClient
#import gridfs
import datetime


def main():

    MONGO_URI = 'mongodb://localhost'
    client = MongoClient(MONGO_URI)
    db = client['fusa2']
    Collection = db['Archivos']

    # Cargar ruta de archivos de audio
    ruta = os.getcwd() + "/audios"

    # cargar audios
    ruta2 = ruta + "/city.wav"
    ruta3 = ruta + "/Alarma.wav"
    ruta4 = ruta + "/Auto.wav"
    ruta5 = ruta + "/Cafeteria.wav"
    ruta6 = ruta + "/Construccion.wav"
    ruta7 = ruta + "/Construccion-2.wav"
    ruta8 = ruta + "/Lluvia.wav"
    ruta9 = ruta + "/Musica.wav"
    ruta10 = ruta + "/Perro.wav"

    # Abrir los archivos en binario
    cargar2 = open(ruta2, "rb")
    cargar3 = open(ruta3, "rb")
    cargar4 = open(ruta4, "rb")
    cargar5 = open(ruta5, "rb")
    cargar6 = open(ruta6, "rb")
    cargar7 = open(ruta7, "rb")
    cargar8 = open(ruta8, "rb")
    cargar9 = open(ruta9, "rb")
    cargar10 = open(ruta10, "rb")

    # asignar nombre a cada archivo leido
    city = cargar2.read()
    Alarma = cargar3.read()
    Auto = cargar3.read()
    Cafeteria = cargar4.read()
    Construccion = cargar5.read()
    Construccion2 = cargar6.read()
    Lluvia = cargar7.read()
    Musica = cargar8.read()
    Perro = cargar9.read()

    archivos = [
        {"fecha_de_grabacion": datetime.datetime(2014, 3, 20), "ciudad": "Valdivia", "duracion": 35,
         "formato": "wav", "latitud": "-39.806116", "longitud": "-73.255287", "exterior": True,
                           "usuario": {"rut": 20641489, "nombre": "Fabio", "apellido": "Saez"},
                           "audio": city,
                           "etiquetas": {
                               "nombre_fuente": "animales", "descripcion": "una ciudad con muchos pajaritos"},
         },
        {"fecha_de_grabacion": datetime.datetime(2017, 6, 10), "ciudad": "Valdivia", "duracion": 3,
         "formato": "wav", "latitud": "-39.812202", "longitud": "-73.245149", "exterior": True,
                           "usuario": {"rut": 20641489, "nombre": "Fabio", "apellido": "Saez"},
                           "audio": Alarma,
                           "etiquetas": {
                               "nombre_fuente": "Alerta", "descripcion": "Alarma de emergencia"},
         },
        {"fecha_de_grabacion": datetime.datetime(2019, 6, 10), "ciudad": "Valdivia", "duracion": 5,
         "formato": "wav", "latitud": "-39.812715636479936", "longitud": "-73.24586822792271", "exterior": False,
         "usuario": {"rut": 20641489, "nombre": "Fabio", "apellido": "Saez"},
         "audio": Cafeteria,
         "etiquetas": {
            "nombre_fuente": "Humano", "descripcion": "Mucha gente charlando en una cafeteria"},
         },
        {"fecha_de_grabacion": datetime.datetime(2016, 11, 10), "ciudad": "Valdivia", "duracion": 1,
         "formato": "wav", "latitud": "-39.813811", "longitud": "-73.243898", "exterior": True,
         "usuario": {"rut": 20314123, "nombre": "Fulanito", "apellido": "Perez"},
         "audio": Construccion,
         "etiquetas": {
            "nombre_fuente": "Mecanico", "descripcion": "Persona martillando"},
         },
        {"fecha_de_grabacion": datetime.datetime(2017, 6, 10), "ciudad": "Valdivia", "duracion": 7,
         "formato": "wav", "latitud": "-39.8134617798529", "longitud": "-73.24337563988647", "exterior": True,
         "usuario": {"rut": 20641489, "nombre": "Fabio", "apellido": "Saez"},
         "audio": Construccion2,
         "etiquetas": {
            "nombre_fuente": "Mecanico", "descripcion": "Persona Martillando"},
         },
        {"fecha_de_grabacion": datetime.datetime(2014, 2, 5), "ciudad": "Valdivia", "duracion": 100,
         "formato": "wav", "latitud": "-39.817631", "longitud": "73.250573", "exterior": True,
         "usuario": {"rut": 33291937, "nombre": "Rob", "apellido": "Iwanczyk"},
         "audio": Lluvia,
         "etiquetas": {
            "nombre_fuente": "Climatico", "descripcion": "Una tensa lluvia"},
         },
        {"fecha_de_grabacion": datetime.datetime(2017, 6, 10), "ciudad": "Valdivia", "duracion": 3,
         "formato": "wav", "latitud": "-39.818019", "longitud": "-73.235079", "exterior": True,
         "usuario": {"rut": 17061034, "nombre": "Kienan", "apellido": "Mcall"},
         "audio": Musica,
         "etiquetas": {
            "nombre_fuente": "Musica", "descripcion": "bajo"},
         },
        {"fecha_de_grabacion": datetime.datetime(2020, 6, 20), "ciudad": "Valdivia", "duracion": 6,
         "formato": "wav", "latitud": "-39.812202", "longitud": "-73.245149", "exterior": True,
         "usuario": {"rut": 17061034, "nombre": "Kienan", "apellido": "Mcall"},
         "audio": Perro,
         "etiquetas": {
            "nombre_fuente": "Animales", "descripcion": "Perro ladrando"},
         },
        {"fecha_de_grabacion": datetime.datetime(2013, 6, 10), "ciudad": "Valdivia", "duracion": 24,
         "formato": "wav", "latitud": "-39.812202", "longitud": "-73.245149", "exterior": True,
         "usuario": {"rut": 21697858, "nombre": "Shea", "apellido": "Aspinall"},
         "audio": Auto,
         "etiquetas": {
            "nombre_fuente": "Vehiculos", "descripcion": "vehiculos"},
         },
    ]

    Collection.insert_many(archivos)


main()
