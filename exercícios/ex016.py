# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 23:03:48 2023

@author: thais
"""

#%% Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc

n = float(input('Digite um número: '))

print('A parte inteira de {} é {}'.format(n, trunc(n)))
