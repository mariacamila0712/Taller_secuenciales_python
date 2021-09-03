# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 17:35:30 2021

@author: Maria Camila
"""

# Tres personas deciden invertir su dinero para fundar una empresa.
# Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje
# que cada quien invierte con respecto a la cantidad total invertida.
inv1 = float(input('Cantidad de dinero que invirtio la persona 1: $'))
inv2 = float(input('Cantidad de dinero que invirtio la persona 2: $'))
inv3 = float(input('Cantidad de dinero que invirtio la persona 3: $'))
total_inv = inv1 + inv2 + inv3

porc_pers1 = (inv1 * 100) / total_inv
porc_pers2 = (inv2 * 100) / total_inv
porc_pers3 = (inv3 * 100) / total_inv

print(f'El porcentaje de inversion de la primera persona es de: {porc_pers1}%')
print(f'El porcentaje de inversion de la segunda persona es de: {porc_pers2}%')
print(f'El porcentaje de inversion de la tercera persona es de: {porc_pers3}%')
