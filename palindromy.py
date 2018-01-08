#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 14:22:44 2018

@author: izabela.pachel
"""

text=input("Podaj tekst do sprawdzenia:\n")



def zamien(text):
    text=text.replace(" ","")
    text=text.replace(",","")
    text=text.replace(".","")
    text=text.replace(":","")
    text=text.replace("\"","")
    text=text.replace("?","")
    text=text.replace("!","")
    text=text.replace("?","")
    text=text.replace("\t","")
    text=text.replace("\n","")
    text=text.replace(";","")
    text=text.lower()
    
    return text

print(zamien(text))

def spr(text):
    yup=0
    nope=0
    for i in range(0,len(text)//2):
        if text[i]==text[len(text)-1-i]:
           yup+=1
        else:
            nope+=1
    if nope!=0: 
        print("Tekst nie jest palindromem ;(")
    else:
        print("Tekst jest palindromem ;)")
    return 0
    
check=spr(zamien(text))
print(check)
