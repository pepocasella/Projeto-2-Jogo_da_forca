# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:20:45 2015

@author: Insper
"""
import random #choice
import turtle

def construcao_janela():
    
    trave = turtle.Turtle()
    window = turtle.Screen()    # cria uma janela
    window.setup(width=1400,startx=None, starty=None)
    window.bgcolor("white")
    window.title("Jogo da Forca")
    
#------------------------------------------------------------------------------    
    
def construcao_estrutura_forca():
    
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
#------------------------------------------------------------------------------    

def escolhe_palavra(palavras):
    palavra = random.choice(palavras)
    return palavra
#-----------------------------------------------------------------------------
    
def desenha_tracinhos(palavra):
    #mover a tartaruga pro lugar certo
    trave.penup()
    trave.goto(20, 20)
    trave.setheading(0)
    for c in palavra:
        trave.pendown()
        if c == " ":
            trave.penup()
        trave.fd(100)
        trave.penup()
        trave.fd(20)
 #-----------------------------------------------------------------------------
        
def posicoes_letra(palavra, letra):
    pos = []
    for i in range(0, len(palavra)):
        if palavra[i] == letra:
            pos.append(i)
            
    return pos
 
 #-----------------------------------------------------------------------------  
    
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

#------------------------------------------------------------------------------

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
        
#------------------------------------------------------------------------------

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
        
#------------------------------------------------------------------------------
    
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

#------------------------------------------------------------------------------

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
    
    
#------------------------------------------------------------------------------
    
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

#------------------------------------------------------------------------------
                    
#window.exitonclick()


        

