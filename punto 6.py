# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 20:25:58 2021

@author: Maria Camila
"""

# El periódico el Informador cobra por un aviso clasificado un monto
# que depende del número de palabras, tamaño en centímetros y
# número de colores. Cada palabra tiene un costo de $20.000, cada
# centímetro tiene un costo de $15.000 y cada color tiene un costo de
# $25.000. Realice un algoritmo que determine el monto a pagar por un
# aviso clasificado.
palabras = int(input('Digite el numero de palabras que contiene su aviso: '))
centimetros = float(input('Digite el tamaño de su aviso en centimetros: '))
colores = int(input('Digite el numero de colores que contiene su aviso: '))
costo_palabras = 20000 * palabras
costo_tamaño = 15000 * palabras
costo_color = 25000 * colores

monto_total = costo_palabras + costo_tamaño + costo_color
print(f'El monto total a pagar por el aviso es: ${monto_total:,}')
