# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 21:47:38 2021

@author: Maria Camila
"""

# En una fototienda cobran por el revelado de un rollo $1.500 por cada
# foto. Realice un algoritmo que determine el monto a pagar por un
# revelado completo sabiendo que adiconalmente le cobran el IVA
# (16%).
foto = int(input('Digite el numero de fotos que va a revelar: '))
revelado = 1500 * foto
iva = 0.16 * revelado
revelado_total = revelado + iva
print(f'El valor total a pagar es de: ${revelado_total:,}')
