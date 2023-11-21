# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:45:58 2023

@author: thais
"""

#%% Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
#   primitivo e todas as informações possíveis sobre ele.

var = input('Digite algo: ')

print('O tipo primitivo do que você digitou é: {}'.format(type(var)))
print('Só tem espaços? {}'.format(var.isspace()))
print('É um número? {}'.format(var.isnumeric()))
print('É alfabético? {}'.format(var.isalpha()))
print('É alfanumérico? {}'.format(var.isalnum()))
print('Está em maiúsculas? {}'.format(var.isupper()))
print('Está em minúsculas? {}'.format(var.islower()))
print('Está capitalizada? {}'.format(var.istitle()))
