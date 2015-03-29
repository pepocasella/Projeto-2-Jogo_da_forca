# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:20:15 2015

@author: Insper
"""
import random
import turtle               # Usa a biblioteca de turtle graphics


#------------------------------------------------------------------------------

window = turtle.Screen()    # cria uma janela
window.setup(width=1400,startx=None, starty=None)
window.bgcolor("white")
window.title("Jogo da Forca")

trave = turtle.Turtle()
trave.speed(2)
trave.pensize(5)
trave.penup()
trave.setpos(-300,0)

trave.pendown()         #inicio construção da forca
trave.forward(80)
trave.left(90)
trave.forward(-40)
trave.left(90)
trave.forward(80)
trave.right(90)
trave.forward(40)
trave.right(90)
trave.forward(40)
trave.left(90)
trave.forward(200)
trave.right(90)
trave.forward(80)
trave.right(90)
trave.forward(20)       #fim da construção da forca

window.textinput("Forca", "Texto Pergunta")

#------------------------------------------------------------------------------
def lista_palavras(nome_do_arquivo="lista_forca.txt"):
    text = open(nome_do_arquivo, 'r', encoding = 'utf-8' )
    read = text.readlines() # lista suja
    lista =[] # lista limpa
    for linha in read:                  #joga todas as palavras na lista limpa
        y = linha.strip().lower()
        if len(y) > 0:  
            lista.append(y)             #adiciona as palavras a nova lista
    #print(lista)                 #imprime cada palavra
    return lista

def escolhe_palavra(palavras):
    palavra = random.choice(palavras)
    return palavra
    
def desenha_tracinhos(palavra):
    #mover a tartaruga pro lugar certo
    
    for c in palavra:
        trave.pendown()
        if c == " ":
            trave.penup()
        trave.fd(100)
        trave.penup()
        trave.fd(20)

#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------


#------------------------------------------------------------------------------

def construcao_cabeca():
        
        
        trave = turtle.Turtle()          #Constroi a cabeca
        trave.hideturtle()        
        trave.speed(5)
        trave.pensize(4)
        trave.penup()
        trave.setpos(-180,180)
        trave.left(180)
        trave.pendown()
        trave.circle(20)
        trave.color("black")

construcao_cabeca()

def construcao_tronco():            #constroi o tronco
    
        trave = turtle.Turtle()
        trave.hideturtle()
        trave.speed(5)
        trave.pensize(4)
        trave.penup()
        trave.setpos(-180,140)
        trave.pendown()
        trave.right(90)
        trave.forward(100)
        trave.color('black')
        
construcao_tronco()

def construcao_braco():                  #constroi o braço
    
    trave=turtle.Turtle()
    trave.hideturtle()
    trave.speed(5)
    trave.pensize(5)
    trave.penup()
    trave.setpos(-180,120)
    trave.pendown()
    trave.right(135)
    trave.forward(40)
    trave.color("black")
    
construcao_braco()
    
def construcao_braco2():                 #constroi o braço
    
    
    trave=turtle.Turtle()
    trave.hideturtle()
    trave.speed(5)
    trave.pensize(5)
    trave.penup()
    trave.setpos(-180,120)
    trave.pendown()
    trave.right(400)
    trave.forward(40)
    trave.color("black")

construcao_braco2()

def construcao_perna():              #constroi o perna
    
    trave=turtle.Turtle()
    trave.hideturtle()
    trave.speed(5)
    trave.pensize(5)
    trave.penup()
    trave.setpos(-180,40)
    trave.pendown()
    trave.right(30)
    trave.forward(40)
    
    
construcao_perna()
    
def construcao_perna2():                 #constroi o perna
    
    trave=turtle.Turtle()
    trave.hideturtle()
    trave.speed(5)
    trave.pensize(5)
    trave.penup()
    trave.setpos(-180,40)
    trave.left(-150)
    trave.pendown()
    trave.forward(40)

construcao_perna2()


#-------------------------------------------------------------------------------




    


window.exitonclick()












