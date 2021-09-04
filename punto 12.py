# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 22:06:48 2021

@author: Maria Camila
"""

# Una video tienda alquila DVD a $1.500 el día. Tiene una promoción
# que consiste en dejar gratis el alquiler de una película. Realice un
# algoritmo que teniendo como dato de entrada el total de películas
# alquiladas, y el número de días de alquiler, determine el monto a
# pagar.
peliculas = int(input('Digite el numero de peliculas alquiladas: '))
dias = int(input('Digite el numero de dias de alquiler: '))
monto = (peliculas - 1) * dias * 1500
print((f'El valor a pagar por el alquiler de las peliculas es de: ${monto:,}'))
