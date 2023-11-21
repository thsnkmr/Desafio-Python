# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 20:43:20 2023

@author: thais
"""

#%% Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = float(input('Digite um número: '))

print('O dobro de {} é {}, o triplo é {}, e a raiz quadrada é {:.2f}'.format(n, 2*n, 3*n, n**(1/2)))
