import csv
import os.path
import xml.etree.ElementTree as ET
from os import listdir, path
from os.path import isfile, join
import pandas as pd
import mysql.connector as mariadb


def connection():
    mariadb_conexion = mariadb.connect(host='localhost', port='3306', user='root', password='', database='pruebazalcu')
    if mariadb_conexion.is_connected():
        print("Conexión realizada")
        with open("xmlPrueba.csv")as csv_file:
            csv_file = csv.reader(csv_file, delimiter=",")
            for row in csv_file:
                if len(row) == 3:
                    value1 = row[0]
                    value2 = row[1]
                    value3 = row[2]
                    query = "INSERT INTO catalogo values ('%s','%s','%s')" % (value1, value2, value3)
                    mycursor = mariadb_conexion.cursor()
                    mycursor.execute(query)
                    mariadb_conexion.commit()
        print("Datos cargados correctamente en la base de datos")


def input_path():
    path = input("Introduce el path del directorio: ")
    return path


def xml_generated_csv():
    try:
        ruta = input_path()
        for element in listdir(ruta):
            file = element
            absolute_path = os.path.join(ruta, file)
            absolute_path = os.path.abspath(absolute_path)
            doc_xml = ET.parse(absolute_path)
            generate_csv(doc_xml)
            print(doc_xml)
        print("El .csv fue creado")
    except OSError as e:
        print("El directorio no fue encontrado", e)


def generate_csv(file_xml):
    xml_to_csv = open("xmlPrueba.csv", "a")
    csv_writer = csv.writer(xml_to_csv)

    for element in file_xml.iter("cd"):
        list_nodes = []
        cancion = element.find("cancion").text
        list_nodes.append(cancion)
        artista = element.find("artista").text
        list_nodes.append(artista)
        precio = element.find("precio").text
        list_nodes.append(precio)
        csv_writer.writerow(list_nodes)
    xml_to_csv.close()


def main():
    xml_generated_csv()
    data_frame = pd.read_csv("xmlPrueba.csv", delimiter=",")
    print(data_frame)
    connection()


if __name__ == "__main__":
    main()
