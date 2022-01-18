# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 22:26:38 2022

@author: lenovo
"""

import csv, random

datosTerror = []

def terror(*args):
    
    #lectura del archivo de excel Terror.csv
    with open('C:/Users/lenovo/chatvoice/conversations/librosBot/plugins/Terror.csv') as File:
        reader = csv.DictReader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
        
        #los datos se guardan en la lista datosTerror para procesarlos
        for row in reader:
            datosTerror.append(row)

    #se escoge un numero random para seleccionar cualquier obra
    finalRandom =  len(datosTerror) #tamaño de los datos guardados
    obraSeleccionada = datosTerror[random.randint(0,finalRandom)]
 
    #se muestra la obra seleccionada y su autor
    print("\n")
    for etiqueta,dato in obraSeleccionada.items():
        print("\t\t{}: {}".format(etiqueta,dato))
            
      
    #return 'say "estamos dentro del archivo terrorP"'
    
#terror()
   
    



    

            
          