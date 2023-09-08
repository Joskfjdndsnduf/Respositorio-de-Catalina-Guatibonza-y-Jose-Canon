#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 08:37:12 2023

@author: katedremur
"""
""

"Se desea saber si el mineral es un silicato, es decir si tiene silicio (Si) y ox´ıgeno (O) en su composici´on"
"qu´ımica.se desea calcular la densidad del material en unidades SI"
"Se desea visualizar el color del material m´as com´un (Pista: utilice matplotlib)"
"Se desea imprimir en la consola su dureza, su tipo de rompimiento y el sistema de organizaci´on de los"
"´atomos"

import matplotlib.pyplot as mlp
import matplotlib.patches as mpatches

class Minerales:

    def __init__ (self, nombre, dureza, rompimiento_por_fractura, color, composicion, lustre, specific_gravity, sistema_cristalino):
         self.nombre = nombre
         self.dureza = dureza
         self.lustre = lustre
         self.rompimiento_por_fractura = rompimiento_por_fractura
         self.color = color
         self.composicion = composicion
         self.sistema_cristalino = sistema_cristalino
         self.specific_gravity = specific_gravity
         
    
    def silicato (self) :
        if 'Si' in self.composicion and 'O' in self.composicion:
            return True
        else:
            return False
        
    def densidad(self):
        return self.specific_gravity
    
    
    def color_mineral (self):
     
        fig, ax = mlp.subplots()
        rect = mpatches.Rectangle((0, 0), 1, 1, color = self.color)
        ax.add_patch(rect)
        mlp.title(self.nombre)
        mlp.show()
        
    def caracteristicas (self):
        return print(self.dureza , self.rompimiento_por_fractura , self.sistema_cristalino )
        
        
        
    def __str__ (self):
        return f"Mineral: {self.nombre}\nDureza: {self.dureza}\nLustre: {self.lustre}\nRompimiento por fractura: {self.rompimiento_por_fractura}\nColor: {self.color}\nComposición: {self.composicion}\nSistema cristalino: {self.sistema_cristalino}\nSpecific Gravity: {self.specific_gravity}"
    
    
ejemplo = Minerales("Grafito" , 1.5, "FALSE", "#5f6168"	,"C", "METÁLICO", 2.2, "HEXAGONAL")

"print (Minerales.densidad(ejemplo))"

                
        
    
    
    

    
    
    
        
        
    
    
"def densidad:"
    
"def color:"
    
"def caracteristicas :"
    



