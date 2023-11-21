# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 21:21:07 2023

@author: thais
"""

#%% Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

d = float(input('Insira o valor: R$ '))

print('Você pode comprar {:.2f} US$.'.format(d/5.14))
