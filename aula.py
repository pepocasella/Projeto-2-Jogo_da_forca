# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 17:42:55 2015

@author: Insper
"""

# enquanto o jogo nao acabou:
# desenha a forca
# escolher uma plavra aleatorio
# desenhar os tracinhos
# enquanto o cara ta vivo ou nao ganhou
#  cara chuta uma letra
#  se ele acertou -> escreve a letra no tracinho certo
#  se ele errou -> desenha a parte correta
# vc quer jogar de novo?
# se nao -> break

trave.penup()
trave.goto(240, 20)

while True:
    
    posicoes = posicoes_letra(palavra, letra_chutada)
    if len(posicoes) > 0:
        for i in posicoes:
            trave.penup()
            trave.goto(100 * i + 20 * i, 20)
            trave.pendown()
            trave.write(letra_chutada,  False, font=("Arial",14))
    
    window = tela.textinput("Destino", "Vc quer jogar de novo? Se sim, digite 1")
    if opcao != "1":
        break