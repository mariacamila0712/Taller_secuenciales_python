# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Haga un algoritmo que calcule la masa de la siguiente fórmula:
# Masa = (presión * volúmen) / (0.37 * (temperatura + 460))
presion = float(input('Digite el valor de la presion: '))
volumen = float(input('Digite el valor del volumen: '))
temperatura = float(input('Digite el valor de la temperatura: '))
masa = (presion * volumen) / (0.37 * (temperatura + 460))
print(f'El valor calculado de la masa es de: {masa}')
