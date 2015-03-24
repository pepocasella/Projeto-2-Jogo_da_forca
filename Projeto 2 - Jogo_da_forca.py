# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:20:15 2015

@author: Insper
"""

import turtle               # Usa a biblioteca de turtle graphics




'''
-------------------------------------------------------------------------------
'''

arquivo = open('lista_forca.txt', 'r+')
l=arquivo.read()
print(l)


window = turtle.Screen()    # cria uma janela
window.setup(width=1400,starx=None, starty=None)
window.bgcolor("white")
window.title("Jogo da Forca")

def janela_abertura():
    pass

    
escolha = window.textinput('Escolha', 'Escreva aqui sua letra')
    


window.exitonclick()


IgneousGuikas
lezherus