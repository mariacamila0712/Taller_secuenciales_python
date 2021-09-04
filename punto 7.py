# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 20:47:35 2021

@author: Maria Camila
"""

# Una empresa paga a sus empleados un bono por antigüedad que
# consiste en $100.000 por el primer año laboral y $120.000 por cada
# año siguiente. Realice un algoritmo que determine el monto del bono
# a pagar a un trabajador que tiene varios años en la empresa
años = int(input('Digite cuantos años ha laborado en la empresa: '))
calculo_años = años - 1
bonos_sig = 120000 * calculo_años
monto_bono = 100000 + bonos_sig
print(f'El monto del bono a pagar al trabajador es: ${monto_bono:,}')
