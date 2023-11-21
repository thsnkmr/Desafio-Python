# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:47:24 2023

@author: thais
"""

#%% Faça um programa que leia umnúmero inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número inteiro: '))

print('O antecessor de {} é {}, e o sucessor é {}'.format(n, n-1, n+1))
