# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 22:57:08 2023

@author: thais
"""

#%% Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
#   e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, 
#   sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

d = int(input('Por quantos dias você ficou com o carro? '))
km = float(input('Informe a distância em km rodados: '))

p = (km * 0.15) + (d * 60)

print('O valor do aluguel por {} dias e {:.1f} km rodados é de {:.2f} reais'.format(d, km, p))
