# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:20:15 2015

@author: Insper
"""

from função_importar_arquivo import *

import turtle               # Usa a biblioteca de turtle graphics



trave = turtle.Turtle()   
window = turtle.Screen()

while True:

    # Fez desenhos -> forca e a tela
    construcao_janela(trave, window)
    construcao_estrutura_forca(trave)
    
    
    palavras = lista_palavras("lista_forca.txt")
    palavra = escolhe_palavra(palavras)
    desenha_tracinhos(palavra, trave)
    
    #
    #------------------------------------------------------------------------------
    
                
    acertos = 0
    erros = 0
    chutadas = []
    for letra in palavra:  #para resolver o bug dos space
        if letra == " ":
            acertos = acertos + 1
    
    while acertos < len(palavra) and erros < 6:
        letra = window.textinput("Chute", "Que letra você quer chutar?")
        if letra is None:
            break
        if len(letra) > 1 or letra.isdigit() or letra in chutadas: #para opção diferente letra e numero
            continue
        pos = posicoes_letra(palavra, letra)
        if len(pos) > 0:
            #acertos
            acertos = acertos + len(pos)
            for p in pos.keys():
                trave.penup()
                trave.goto(-120 + 60*p, -20)
                trave.pendown()
                trave.write(pos[p].upper(), align="center", font=('Arial', 24, 'bold'))           
        else:
            #errou
            if erros == 0:
                construcao_cabeca()
            elif erros == 1:
                construcao_tronco()
            elif erros == 2:
                construcao_braco()
            elif erros == 3:
                construcao_braco2()
            elif erros == 4:
                construcao_perna()
            elif erros == 5:
                construcao_perna2()
            chutadas.append(letra)
            trave.penup()
            trave.goto(40 + 60 * erros, 200)
            trave.pendown()
            trave.write(letra.upper(), align="center", font=('Arial', 24, 'bold'))
            erros = erros + 1
            
    opcao = window.textinput("Destino", "Vc quer jogar de novo? Se sim, digite 1")
    if opcao != "1":
        break
    trave.reset()
    window.reset()
    
        
        #posicoes = posicoes_letra(palavra, letra_chutada)
#if len(posicoes) > 0:
#    for i in posicoes:
#        trave.penup()
#        trave.goto(100 * i + 20 * i, 20)
#        trave.pendown()
#        trave.write(letra_chutada,  False, font=("Arial",14))
#
#

#while True:

    


#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------


#------------------------------------------------------------------------------


#
#
#    
#
#
#window.exitonclick()
#
#
#
#
#
#
#
#
#
#
#
#
