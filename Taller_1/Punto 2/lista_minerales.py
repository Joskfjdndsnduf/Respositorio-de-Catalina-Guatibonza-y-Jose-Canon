#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:18:45 2023

@author: katedremur
"""
from mineral import Minerales



info = []
with open('minerales.txt', 'r') as file:
    filas = file.readlines()
    # Suprimir la primera línea (encabezado)
    info = filas[1:]

# Crear objetos Minerales y guardarlos en un arreglo
lista = []
for datos in info:
    datos = datos.strip().split('\t')
    mineral = Minerales(*datos)
    lista.append(mineral)
    
    
def cantidad_silicatos(lista):
    i = 0
    for mineral in lista:
        if mineral.silicato()== True:
            i += 1     
    return i

def promedio_densidad (lista):
    
    densidades = [mineral.densidad() for mineral in lista]
    numeros = [float(x) for x in densidades]
    suma = 0
    for valor in numeros:
        suma  += valor
    
    promedio = suma / len(densidades)
    return round(promedio,2)
    


