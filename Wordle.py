# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 14:20:41 2022

@author: Paul Dupire
"""
import random
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default='browser'

#------Recupération et création des listes : allowed_words et possible words
fichier_allowed_words = open("allowed_words.txt","r")
allowed_words = fichier_allowed_words.read()
allowed_words = allowed_words.split("\n")
fichier_allowed_words.close()

fichier_possible_words = open("possible_words.txt","r")
possible_words = fichier_possible_words.read()
possible_words = possible_words.split("\n")
fichier_possible_words.close()

#-------------Variables globales-----------------
# mot_choisi = random.choice(possible_words)

mot_choisi = random.choice(possible_words)
tentatives_possibles = allowed_words.copy()
def creation_liste():
    liste = []
    for i in range(len(mot_choisi)):
        liste.append([])
    return liste

grey = []
green, yellow = creation_liste(),creation_liste()
liste_couleur = ["v","j","g"]
compteur = 0
count = []

#------------------Fonctions secondaires----------

def fonction_mot_test():
    while True : 
        #mot_test = input("Input a 5 letter word : ")
        mot_test=random.choice(tentatives_possibles)
        if not (mot_test.lower() in allowed_words):
            continue
        else :
            mot_test = mot_test.lower()
            break
    return mot_test
    
def split(word):
    return [char for char in word]


def simplification_liste_gris():
    for i in range(len(grey)):
        for j in reversed(range(len(tentatives_possibles))):
            if grey[i] in split(tentatives_possibles[j]):
                tentatives_possibles.pop(j)

def simplification_liste_vert():
    for i in range(len(green)):
        for j in reversed(range(len(tentatives_possibles))):
            for u in range(len(split(green[i]))):
                if split(green[i])[u].isalpha():    
                    if green[i] != split(tentatives_possibles[j])[i]:
                            tentatives_possibles.pop(j)
                            
def simplification_liste_jaune():
    for i in range(len(yellow)):
        for j in reversed(range(len(tentatives_possibles))):
            for u in range(len(split(yellow[i]))):
                if split(yellow[i])[u].isalpha():    
                    if yellow[i][u] == split(tentatives_possibles[j])[i]:
                            tentatives_possibles.pop(j)
                    elif yellow[i][u] not in split(tentatives_possibles[j]):
                            tentatives_possibles.pop(j)
    

#--------algos de résolution ----------
def supersimple():
    simplification_liste_gris()
    simplification_liste_vert()
    simplification_liste_jaune()
    
    # fig2= go.Figure(data=[go.Table(header=dict(values=["Tentatives"]),
    #               cells=dict(values=[tentatives_possibles]))
    #                   ])
    # fig2.show()

#----------Jeux-----------
def jeu_1():
    global compteur
    while True:
        #print("Mot choisi : ", mot_choisi)
        mot_test = split(fonction_mot_test())
        #print(mot_test)
        
        for i in range(len(mot_test)):
            if mot_test[i] in mot_choisi and mot_test[i] != mot_choisi[i] :
                if not(mot_test[i] in yellow):
                    yellow[i].append(mot_test[i])
                    
                    
            elif mot_test[i] == mot_choisi[i] :
                green[i] = mot_test[i]
                    
            else : 
                    grey.append(mot_test[i])
        
        supersimple()
        compteur += 1 
        
        # fig = go.Figure(data=[go.Table(header=dict(values=['Green', 'Yellow','Grey'],line_color = ['green','yellow','grey']),
        #               cells=dict(values=[green,yellow,grey]))
        #                   ])
        
        # fig.show()
        
        if green != mot_test :
            continue
        
        else :
            print("Bravo !")
            print(compteur)
            count.append(compteur)
            break

#jeu_1()

def jeu_2():
    
    while True :
        mot_test = split(fonction_mot_test())
        print(mot_test)
        while True : 
            str_color = split(input("Input colors : ").lower())
            print(str_color)
            for i in range(len(str_color)):
                if not(str_color[i] in liste_couleur):
                    if not(len(str_color) == len(mot_test)):
                        print("non")
                        continue
                else: 
                    pass
            for i in range(len(str_color)):
                if str_color[i] == "v":
                    green[i] = mot_test[i]
                elif str_color[i] == "j":
                    yellow[i].append(mot_test[i])
                elif str_color[i] == "g":
                    grey.append(mot_test[i])
                else:
                    pass
            
            # fig = go.Figure(data=[go.Table(header=dict(values=['Green', 'Yellow','Grey'],line_color = ['green','yellow','grey']),
            #               cells=dict(values=[green,yellow,grey]))
            #                   ])
            # fig.show()
            
            supersimple()
            break
        if split(green) == mot_test:
            print("Bravo")
            
            break
        
#jeu_2()   



    
for i in range(100):
    mot_choisi = random.choice(possible_words)
    tentatives_possibles = allowed_words.copy()
    def creation_liste():
        liste = []
        for i in range(len(mot_choisi)):
            liste.append([])
        return liste

    grey = []
    green, yellow = creation_liste(),creation_liste()
    liste_couleur = ["v","j","g"]
    compteur = 0
    
    
    jeu_1()
    
fig = go.Figure()
fig.add_trace(go.Histogram(x=count, name="count", texttemplate="%{x}", textfont_size=18))

fig.show()


        
        
        
        
        
        
        
        
