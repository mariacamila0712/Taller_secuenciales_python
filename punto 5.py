# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 20:08:54 2021

@author: Maria Camila
"""

# Una empresa le hace los siguientes descuentos sobre el sueldo base
# a sus trabajadores: 1% por ley de politica pública, 4% por seguro
# social, 0.5% por seguro forzoso y 5% por caja de ahorro. Realice un
# algoritmo que determine el monto de cada descuento y el monto total
# a pagar al trabajador.
sueldo_base = float(input('Digite el sueldo base del trabajador: $'))
ley_pp = 0.01 * sueldo_base
seguro_social = 0.04 * sueldo_base
seguro_forzoso = 0.005 * sueldo_base
caja_ahorro = 0.05 * sueldo_base

monto_total = sueldo_base - ley_pp - seguro_social -seguro_forzoso - caja_ahorro

print(f'El monto del descuento por ley de politica es: ${ley_pp:,}')
print(f'El monto del descuento por seguro social es: ${seguro_social:,}')
print(f'El monto del descuento por seguro forzoso es: ${seguro_forzoso:,}')
print(f'El monto del descuento por caja de ahorro es: ${caja_ahorro:,}')
print(f'El monto total a pagar al trabajador es: ${monto_total:,}')
