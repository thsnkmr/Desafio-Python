# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 22:43:32 2023

@author: thais
"""

#%% Escreva um programa que convert uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

choice = int(input('Você quer realizar a conversão de ºC para ºF [1] ou de ºF para ºC [2]? '))

match choice:
    case 1:
        C = float(input('Digite a temperatura em ºC '))
        cConv = (1.8 * C) + 32
        print('{:.1f} ºC equivale a {:.1f} ºF'.format(C, cConv))
    case 2:
        F = float(input('Digite a temperatura em ºF '))
        fConv = (F - 32) / 1.8
        print('{:.1f} ºF equivale a {:.1f} ºC'.format(F, fConv))
    case _:
        print('Opção inválida!')
        print('-' * 15)
        