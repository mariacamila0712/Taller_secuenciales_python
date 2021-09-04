# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 20:58:11 2021

@author: Maria Camila
"""

# Una Universidad le paga a sus profesores $20.000 la hora y le hace
# un descuento del 5% por concepto de caja de ahorro. Determine el
# monto del descuento y el monto total a pagar al profesor.
hora = float(input('Digite cuantas horas trabajo: '))
pago_horas = 20000 * hora
caja_ahorro = 0.05 * pago_horas
monto_pago = pago_horas - caja_ahorro
print(f'El monto del descuento es de: ${caja_ahorro:,}')
print(f'El monto a pagar al profesor es de: ${monto_pago:,}')
