# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 21:14:05 2023

@author: thais
"""

#%% Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

l = float(input('Digite a distância em metros: '))

print('{:.2f} km \n{:.2f} hm \n{:.2f}dam \n{:.2f} m \n{:.2f} dm \n{:.2f}cm \n{:.2f} mm'.format(l/1000, l/100, l/10, l, 10*l, 100*l, 1000*l))
