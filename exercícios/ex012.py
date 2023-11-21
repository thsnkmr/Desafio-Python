# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 21:27:07 2023

@author: thais
"""

#%% Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Digite o preço original: R$ '))

print('O preço de {:.2f} R$ com desconto de 5% é de {:.2f} R$'.format(p, 0.95*p))
