# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 23:24:42 2023

@author: thais
"""

#%% Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()
