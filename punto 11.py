# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 21:57:04 2021

@author: Maria Camila
"""
# En un hospital existen tres áreas: Ginecología, Pediatría y
# Traumatología. El presupuesto anual del hospital se reparte
# conforme a la siguiente tabla:
# Area ---- Porcentaje Presupuestal
# Ginecología --- 40%
# Traumatología --- 30%
# Pediatría --- 30%
# Obtener la cantidad de dinero que recibirá cada área, para cualquier
# monto presupuestal
monto = float(input('Digite el monto presupuestal: $'))
ginecologia = 0.40 * monto
traumatologia = 0.30 * monto
pediatria = 0.30 * monto
print(f'El valor que recibira el area de ginecologia sera de: ${ginecologia:,}')
print(f'El valor que recibira el area de traumatologia sera de: ${traumatologia:,}')
print(f'El valor que recibira el area de pediatria sera de: ${pediatria:,}')
