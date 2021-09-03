# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 16:23:52 2021

@author: Maria Camila
"""

# z=5; n=3; m= z-n; y = (((z+2-n)^2 * m+8/2 -30 ) / 2 * 5 -3)^ 5 + 15 * 3 - 9/3

z = 5
n = 3
m = z - n
a = (z + 2 - n) ** 2
b = m + 8 / 2 - 30
c = 2 * 5 - 3
d = 5 + 15 * 3 - 9 / 3
y = ((a * b) / c) ** d
print(f'El resultado de y es igual a: {y}')
