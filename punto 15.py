# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 22:30:11 2021

@author: Maria Camila
"""

# El banco del Pueblo da microcréditos a empresarios para ser
# cancelados en un lapso de 2 años (24 meses). Al monto del
# préstamo se le cobra un interés del 24%. El empresario debe pagar
# la mitad del préstamo en 4 cuotas especiales y la otra mitad en 20
# cuotas ordinarias. Realice un algoritmo que teniendo como dato de
# entrada el monto del préstamo, determine el monto total a pagar por
# el préstamo, el monto de las cuotas especiales y el monto de las
# cuotas ordinarias.
monto_prestamo = float(input('Digite el valor del prestamo: $'))
intereses = 0.24 * monto_prestamo
pagar = monto_prestamo + intereses
cuotas_especiales = (pagar / 2) / 4
cuotas_ordinarias = (pagar / 2) / 20
print(f'El valor total a pagar por el prestamo sera de: ${pagar:,}')
print(f'El valor de las cuotas especiales sera de: ${cuotas_especiales:,}')
print(f'El valor de las cuotas ordinarias sera de: ${cuotas_ordinarias:,}')
