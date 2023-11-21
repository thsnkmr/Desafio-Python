# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 21:23:22 2023

@author: thais
"""

#%% Faça um programa que leia a largura e a altura de uma parede em metros, 
#   calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo
#   que cada litro de tinta pinta uma área de 2 m²

l = float(input('Digite a largura em metros: '))
h = float(input('Digite a altura em metros: '))

a = l * h

print('Você precisará de {:.2f} litros de tinta para pintar os {:.2f} m² de sua parede'.format(a/2, a))
