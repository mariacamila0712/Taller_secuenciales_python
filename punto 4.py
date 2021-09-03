# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 17:35:28 2021

@author: Maria Camila
"""

# Un banco da a sus ahorradores un interes de 1.5% sobre el monto
# ahorrado. Teniendo como dato de entrada el saldo inicial del
# ahorrador determine el saldo final.
saldo_inicial = float(input('Digite el valor que desea ahorrar: $'))
interes = 0.015 * saldo_inicial
saldo_final = saldo_inicial + interes
print(f'El saldo final del ahorrador sera de: ${saldo_final}:,')
