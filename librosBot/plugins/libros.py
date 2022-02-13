# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 22:26:38 2022

@author: 
         Flores González Jesus Eduardo
         Manzo Ruiz Yocelyne

Objetivo: Obtener la información del archivo de excel correspondiente, extraer el libro y
          los autores.
"""

import csv, random, os


datosTerror = []

def libros(*args):
    
    #lectura del archivo de excel Terror.csv
    #obteniendo el directorio de trabajo actual junto con el archivo csv
    genero = str(args[0])
    opcion = str(args[1])
    
    #archivo = os.getcwd()+"/conversations/librosBot/plugins"+"/"+genero+".csv"    
    archivo = "C:/Users/lenovo/chatvoice/conversations/librosBot/plugins/terror.csv"
    with open(archivo) as File:
        reader = csv.DictReader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
        
        #los datos se guardan en la lista datosTerror para procesarlos
        for row in reader:
            datosTerror.append(row)
    

    
    if (opcion == "aleatorio"):
        #se escoge un numero random para seleccionar cualquier obra
        finalRandom =  len(datosTerror)-1 #tamaño de los datos guardados
        obraSeleccionada = datosTerror[random.randint(0,finalRandom)]
        
        #se muestra la obra seleccionada y su autor
        print("\n")
        
        for etiqueta,dato in obraSeleccionada.items():
            print("\t\t{}: {}".format(etiqueta,dato))
 
    if (opcion == "autor"):
        print("\t De ese género, tengo los siguientes autores disponibles: ")
        autores = []
        #guarda en una lista a todos los autores
        for etiqueta in datosTerror:
            autores.append(etiqueta['Autor'])
        #se quitan los autores repetidos y se imprime al usuario
        autores = set(autores)
        for nombre in autores:
            print("\t\t** "+nombre)
            
def autor(*args):
    autor = str(args[0])
    for nombre in datosTerror:
        if (nombre['Autor'] == autor):
            print("\t\t** " + nombre['Obra'])
    

#libros()
#autor ()
    
            


    

            
          