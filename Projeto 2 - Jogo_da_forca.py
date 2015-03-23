# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:20:15 2015

@author: Insper
"""

import turtle               # Usa a biblioteca de turtle graphics


window = turtle.Screen()    # cria uma janela
window.bgcolor("lightblue")
window.title("Jogo da Forca")

tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
tartaruga.speed(5)  # define a velocidade
tartaruga.penup()       # Remova e veja o que acontece
tartaruga.setpos(50,0)
tartaruga.pendown()
tartaruga.color("orange")


dist1 = -300
dist2 = -300
dist3 = 100
dist4 = 40

angulo = 90


tartaruga.forward(dist1) # Avança a distancia pedida
tartaruga.right(angulo)  # Vira o angulo pedido
tartaruga.forward(dist2) # Avança a distancia pedida
tartaruga.left(angulo)  # Vira o angulo pedido
tartaruga.forward(dist3) # Avança a distancia pedida
tartaruga.right(angulo)  # Vira o angulo pedido
tartaruga.forward(dist4) # Avança a distancia pedida

arquivo = open('lista1_forca.csv', 'r+')
for linha in arquivo.readlines():
   print(linha)
   
   
       

