# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 22:26:38 2022

@author: 
         Flores González Jesús Eduardo
         Manzo Ruiz Yocelyne
         
Objetivo: Listar los géneros disponibles en el chatbot
"""

nombresGeneros = ["terror", "fantasia", "suspenso", "infantiles", "históricos", 
                  "narrativos", "romance", "superación personal", "policiaco", "divulgación científica", 
                  "psicológicos", "filosofía"]

lista = len(nombresGeneros) #tamaño de la lista nombresGeneros

def generosLiterarios():
   for i in range (0,lista):
       print("\t"+str(i+1)+".- "+nombresGeneros[i])
    
  
            
          