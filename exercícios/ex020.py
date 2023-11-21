# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 23:23:44 2023

@author: thais
"""

#%% O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos 
#   dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]

sort = shuffle(lista)

print('A ordem de apresentação será:\n1º {}\n2º {}\n3º {}\n4º {}'.format(lista[0], lista[1], lista[2], lista[3]))
