# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 23:20:46 2023

@author: thais
"""

#%% Faça um programa que leia o comprimento dos catetos de um triângulo retângulo e mostre a hipotenusa.

from math import sqrt, hypot

cat1 = float(input('Informe o comprimento do primeiro cateto: '))
cat2 = float(input('Informe o comprimento do segundo cateto: '))

hip = sqrt(pow(cat1, 2) + pow(cat2, 2))
hi = hypot(cat1, cat2)

print('A hipotenusa é {:.2f} ou {:.2f}'.format(hip, hi))
