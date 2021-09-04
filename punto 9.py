# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 21:10:07 2021

@author: Maria Camila
"""

# Un centro de comunicaciones alquilan tarjetas para realizar llamadas
# y cobran el monto consumido de la tarjeta mas un recargo del 20%.
# Teniendo como dato de entrada el monto inicial y el monto final de la
# tarjeta, determine el costo de la llamada.
monto_inicial = float(input('Digite el valor inicial de la tarjeta: $'))
monto_final = float(input('Digite el valor final de la tarjeta: $'))
monto_cons = monto_inicial - monto_final
recargo = 0.20 * monto_cons
costo_llamada = monto_cons + recargo
print(f'El valor del costo final de la llamada es: ${costo_llamada:,}')
