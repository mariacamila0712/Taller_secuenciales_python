# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 17:32:42 2021

@author: Maria Camila
"""

# Calcular el número de pulsaciones que una persona debe tener por
# cada 10 segundos de ejercicio, si la fórmula es:
# Num. Pulsaciones = (200 – edad) /10.

edad = int(input('Digite su edad: '))
num_pul = (200 - edad) / 10
print(f'El numero de pulsaciones que deber tener usted es: {num_pul}')
