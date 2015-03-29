# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:20:45 2015

@author: Insper
"""
import unicodedata

text = open('lista_forca.txt', 'r', encoding = 'utf-8' )
read = text.readlines() # lista suja
lista=[] # lista limpa
for i in read:
    y=i.strip()
    lista.append(y)
print(lista[0])

