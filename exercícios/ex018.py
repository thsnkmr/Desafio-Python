# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 23:21:50 2023

@author: thais
"""

#%% Faça um programa que leia um ângulo qualquer e mostre o valor do seno, cosseno e tangente.

from math import sin, cos, tan, pi

angle = int(input('Insira um ângulo em graus: '))

rad = pi/180 * angle

sen = sin(rad)
cos = cos(rad)
tg = tan(rad)

print('Sobre o ângulo de {}º: sen({}) = {:.2f}, cos({}) = {:.2f}, tg({}) = {:.2f}'.format(angle, angle, sen, angle, cos, angle, tg))
