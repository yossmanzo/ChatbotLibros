# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 22:26:38 2022

@author: 
         Flores González Jesus Eduardo
         Manzo Ruiz Yocelyne
"""

import csv, random, os


datosTerror = []

def libros(*args):
    
    #lectura del archivo de excel Terror.csv
    #obteniendo el directorio de trabajo actual junto con el archivo csv
    genero = str(args[0])
    
    archivo = os.getcwd()+"/conversations/librosBot/plugins"+"/"+genero+".csv"    
    
    with open(archivo) as File:
        reader = csv.DictReader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
        
        #los datos se guardan en la lista datosTerror para procesarlos
        for row in reader:
            datosTerror.append(row)

    #se escoge un numero random para seleccionar cualquier obra
    finalRandom =  len(datosTerror)-1 #tamaño de los datos guardados
    obraSeleccionada = datosTerror[random.randint(0,finalRandom)]
 
    #se muestra la obra seleccionada y su autor
    print("\n")
    
    for etiqueta,dato in obraSeleccionada.items():
        print("\t\t{}: {}".format(etiqueta,dato))
            


    

            
          