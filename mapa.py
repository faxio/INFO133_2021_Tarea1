import folium
from pymongo import MongoClient
import os
import datetime


def main():

    diarias = folium.Map(
        location=[-39.82749610215353, -73.247956875481], zoom_start=14)
    categorias = folium.Map(
        location=[-39.82749610215353, -73.247956875481], zoom_start=14)

    MONGO_URI = 'mongodb://localhost'
    client = MongoClient(MONGO_URI)
    db = client['fusa2']
    Collection = db['Archivos']

    # Cargar los datos de la base de datos

    # Dia => 2017-6-10 => fecha a elegir => hay 3 sonidos
    #año = int(input("Escriba el año que quiere saber: "))
    #mes = int(input("Escriba el mes que quiere saber: "))
    #dia = int(input("Escriba el dia que quiere saber: "))

    dia = 10
    mes = 6
    año = 2017

    # buscar por fecha
    resultado = Collection.find(
        {"fecha_de_grabacion": {"$gte": datetime.datetime(año, mes, dia), "$lt": datetime.datetime(año, mes, dia, 23)}})

    # Agregar los marcadores al mapa
    for i in resultado:
        folium.Marker([i['latitud'], i['longitud']], popup="<i>" + i["etiquetas"]
                      ["descripcion"] + "</i>", tooltip=i["etiquetas"]["nombre_fuente"]).add_to(diarias)

    # Guardar el mapa en un archivo
    diarias.save("GrabacioneDiarias.html")

    # Buscar Mecanico y animales
    resultado2 = Collection.find(
        {"$or": [{"etiquetas.nombre_fuente":  "Mecanico"}, {"etiquetas.nombre_fuente":  "Animales"}]})

    for i in resultado2:
        folium.Marker([i['latitud'], i['longitud']], popup="<i>" + i["etiquetas"]
                      ["descripcion"] + "</i>", tooltip=i["etiquetas"]["nombre_fuente"]).add_to(categorias)

    categorias.save("Categorias.html")

    # Descargar audios
    ruta = os.getcwd() + "/descargas"
    info = Collection.find_one({"duracion": 35})
    # print(info)

    audioB = info['audio']
    nombre = info['etiquetas']['nombre_fuente']

    # Guardar archivo
    ruta2 = ruta + "/" + nombre + ".wav"
    salida = open(ruta2, "wb")
    salida.write(audioB)
    salida.close()


main()
