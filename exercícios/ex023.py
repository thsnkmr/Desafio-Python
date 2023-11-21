# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 11:21:58 2023

@author: thais
"""

#%% Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = input('Digite um número de 0 a 9999: ')

inteiro = int(numero)

m = inteiro // 1000
c = (inteiro % 1000) // 100
d = (inteiro % 100) // 10
u = inteiro % 10

print('Milhar: {}\nCentena: {}\nDezena: {}\nUnidade: {}'.format(m, c, d, u))

