# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:27:09 2023

@author: thais
"""

#%% Crie um programa que leia o nome completo de uma pessoa e mostre: 
#   - o nome com todas as letras maiúsculas
#   - o nome com todas as letras minúsculas
#   - quantas letras ao todo (sem considerar espaços)
#   - quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
separados = nome.split()

print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é {} tem {} letras'.format(separados[0], nome.find(' ')))
