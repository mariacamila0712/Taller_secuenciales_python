# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 16:42:25 2021

@author: Maria Camila
"""

# z=5; n=( (8+2-4)^2 * 5+8+7/2 -30*5 ) / 2 * 5 -3; m= z^2*3+n
# y = ((( (z+2-n)^2 x m+8/2 -30 ) / 2 * 5 -3)^ 5 + 15 * 3 - 9/3) ^ 2 – 5/4
z = 5
a = (8 + 2 - 4) ** 2
b = 5 + 8 + 7 / 2 - 30 * 5
c = 2 * 5 - 3
n = (a * b) / c
m = z ** 2 * 3 + n
d = (z + 2 - n) ** 2
e = m + 8 / 2 - 30
f = 2 * 5 - 3
g = 5 + 15 * 3 - 9 / 3
h = 2 - 5 / 4
y = (((d * e) / f) ** g) ** h
print(f'EL resultado de y es igual a: {y}')
