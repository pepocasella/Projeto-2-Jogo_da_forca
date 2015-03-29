# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:01:29 2015

@author: Insper
"""

import random
import turtle

archive=open("lista_forca.txt",encoding="utf-8")
s1=archive.readlines()
keyword0= random.choice(s1)
keyword = keyword0.strip()
print(keyword)


e = " __ "

#------------------------------------------------------------------------------

def body():
    
    if erros == 1:
        base = turtle.Turtle()          #Constroi a cabeca
        base.speed(5)
        base.penup()
        base.setpos(-225,110)
        base.pendown()
        base.circle(20)
        base.color("black")
    
    if erros == 2:
        base = turtle.Turtle()           #Constroi o tronco
        base.speed(5)
        base.penup()
        base.setpos(-225,110)
        base.pendown()
        base.left(270)
        base.forward(90)
        base.color("black")

    if erros == 3:
        base = turtle.Turtle()           #Constroi o braco esquerdo
        base.speed(5)
        base.penup()
        base.setpos(-225,90)
        base.pendown()
        base.left(225)
        base.forward(40)
        base.color("black")
    
    if erros == 4:
        base = turtle.Turtle()            #Constroi o braco direito
        base.speed(5)
        base.penup()
        base.setpos(-225,90)
        base.pendown()
        base.left(315)
        base.forward(40)
        base.color("black")

    if erros == 5:
        base = turtle.Turtle()        #Constroi a perna esquerda
        base.speed(5)
        base.penup()
        base.setpos(-225,20)
        base.pendown()
        base.left(240)
        base.forward(60)
        base.color("black")
    
    if erros == 6:
        base = turtle.Turtle()        #Constroi a perna direita
        base.speed(5)
        base.penup()
        base.setpos(-225,20)
        base.pendown()
        base.left(300)
        base.forward(60)
        base.color("black")    
        
    if erros == 7:
        base = turtle.Turtle()            #Constroi a lamina da espada
        base.speed(5)
        base.penup()
        base.setpos(-200,65)
        base.pendown()
        base.left(45)
        base.forward(100)
        base.color("black")

#------------------------------------------------------------------------------        
 
   
window = turtle.Screen()    # Usa a biblioteca de turtle graphics
window.bgcolor("white")     # cria uma janela
window.title("Forca")

#keyword=window.textinput("Forca", "Texto Pergunta")

base = turtle.Pen()   # Constrói a Forca
base.speed(5)
base.penup()
base.setpos(200,-200)
base.pendown()
base.backward(500)     # anda 500 posições para tras
base.left(90)        # gira o ponteiro em 90 graus para a esquerda
base.forward(400)     # anda mais 400 posições para a frente
base.right(90)
base.forward(75)
base.right(90)
base.forward(50)
base.color("black")

base.penup()
base.setpos(50,200)
base.write(len(keyword)*e,"Arial")

erros = 0
acertos = 0
while erros<7 and acertos<len(keyword):
    guess = window.textinput("Guess", "Write a letter.")

    if guess in keyword:
            for i in range(len(keyword)):
                if guess == keyword[i]:
                    base.penup()
                    base.setpos(50+i*19,200)                    
                    base.write(guess,"Arial")
                    acertos+=1
                    
    else:
        erros+=1
        body()
        print(erros)
        

window.exitonclick()
            