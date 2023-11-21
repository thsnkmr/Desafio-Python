# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 23:22:41 2023

@author: thais
"""

#%% Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#   Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

from random import randint

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]

sort = randint(0, 3)

print('O(A) aluno(a) sorteado(a) para limpar o quadro foi {}'.format(lista[sort]))
