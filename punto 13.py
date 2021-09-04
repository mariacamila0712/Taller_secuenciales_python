# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 22:20:31 2021

@author: Maria Camila
"""

# Una Agencia de viajes cobra por un Tour a Cartagena $25.000
# diarios por persona. Realice un algoritmo que determine el monto a
# pagar por una familia que desee realizar dicho Tour sabiendo que
# también cobran el 12% de IVA.
num_personas = int(input('Digite el numero de personas que viajaran: '))
valor = num_personas * 25000
iva = 0.12 * valor
monto_final = valor + iva
print(f'El valor total a pagar por el viaje sera de: ${monto_final:,}')
