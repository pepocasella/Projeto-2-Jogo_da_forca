# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:20:45 2015

@author: Insper
"""
import random #choice
import turtle

def construcao_janela(trave, window):
    #turtle.bgpic(picname='executioner.gif')
    window.setup(width=800,startx=None, starty=None)
    window.bgcolor("orange")
    window.title("Jogo da Forca")
    trave.hideturtle()
#    window.textinput('Interface', 'Digite sua letra:')

    
#------------------------------------------------------------------------------    
    
def construcao_estrutura_forca(trave):
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
    
#construcao_estrutura_forca()    
#------------------------------------------------------------------------------    

def lista_palavras(nome_do_arquivo="lista_forca.txt"):
    text = open(nome_do_arquivo, 'r', encoding = 'utf-8' )
    read = text.readlines() # lista suja
    lista =[] # lista limpa
    for linha in read:                  #joga todas as palavras na lista limpa
        y = linha.strip().lower()
        if len(y) > 0:  
            lista.append(y)             #adiciona as palavras a nova lista
    return lista
    
#lista_palavras(nome_do_arquivo="lista_forca.txt")    
    
#------------------------------------------------------------------------------    

def escolhe_palavra(palavras):
    palavra = random.choice(palavras)
    return palavra

#escolhe_palavra(palavras)
#-----------------------------------------------------------------------------
    
    
def desenha_tracinhos(palavra, trave):
    #mover a tartaruga pro lugar certo
    trave.pensize(2)
    trave.penup()
    trave.goto(-140,-20)
    trave.setheading(0)
    for c in palavra:
        trave.pendown()
        if c == " ":
            trave.penup()
        trave.fd(30)
        trave.penup()
        trave.fd(10)
        
#desenha_tracinhos(palavra)        
        
#-----------------------------------------------------------------------------
#dicionario para os acentos -> quando choice igual a letra acentuada a turtle
#lerá a letra chutada sem acento e com acento
acentos = {"a" : ["á", "ã", "â", "à"], "e" : ['é', 'ê'], 'i' : ['í'], 'o' : ['ó', "ô"], 'u' : ['ú'] }       
def posicoes_letra(palavra, letra):
    pos = {} # posicao na palavra -> a letra que vai ser impressa
    for i in range(0, len(palavra)):
        if palavra[i] == letra:
            pos[i] = letra
        if letra in acentos.keys():
            for letra_acentuada in acentos[letra]:
                if letra_acentuada == palavra[i]:
                    pos[i] = letra_acentuada
            
    return pos
    
#posicoes_letra(palavra, letra)
 
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


        

