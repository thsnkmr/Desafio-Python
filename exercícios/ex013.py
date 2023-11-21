# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 21:29:18 2023

@author: thais
"""

#%% Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

s = float(input('Qual o seu salário atual? R$ '))

print('Parabéns! O seu salário com 15% de aumento é de R$ {:.2f}'.format(s*1.15))
