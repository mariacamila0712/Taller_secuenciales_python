# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 22:25:37 2021

@author: Maria Camila
"""

# Un Hotel 5 Estrellas de Santa Marta tiene una promoción para sus
# clientes. Cobra por una habitación $100.000 el primer día y por el
# resto $200.000 por día. Realice un algoritmo que determine el valor
# total a pagar por la habitación si la estadía fue de varios días.
dias = int(input('Digite el numero de dias de hospedaje: '))
valor_hab = (dias - 1) * 200000
valor_estadia = valor_hab + 100000
print(f'El valor a pagar por la habitacion es de: ${valor_estadia:,}')
