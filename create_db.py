from typing import Collection
from pymongo import MongoClient


def main():
    MONGO_URI = 'mongodb://localhost'

    client = MongoClient(MONGO_URI)
    db = client['fusa2']
    collection = db['Usuarios']

    usuarios = [
        {"_id": "20641489", "nombre": "Fabio", "apellido": "Saez"},
        {"_id": "20314123", "nombre": "Fulanito", "apellido": "Perez"},
        {"_id": "61992541", "nombre": "Osborne", "apellido": "Cowhig"},
        {"_id": "61913342", "nombre": "Ber", "apellido": "MacGillavery"},
        {"_id": "84426908", "nombre": "Mace", "apellido": "Trinkwon"},
        {"_id": "33291937", "nombre": "Rob", "apellido": "Iwanczyk"},
        {"_id": "86967827", "nombre": "Carolyne", "apellido": "Gavagan"},
        {"_id": "17061034", "nombre": "Kienan", "apellido": "Mcall"},
        {"_id": "14464531", "nombre": "Ulric", "apellido": "Jimes"},
        {"_id": "26124244", "nombre": "Staffard", "apellido": "Rydings"},
        {"_id": "21697858", "nombre": "Shea", "apellido": "Aspinall"},
        {"_id": "78496922", "nombre": "Waring", "apellido": "Chidwick"}
    ]

    collection.insert_many(usuarios)


main()
