#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 11:55:24 2022

@author: nerhal
"""

import random
import statistics as stc


fichier_allowed_words = open("allowed_words.txt","r")
allowed_words = fichier_allowed_words.read()
allowed_words = allowed_words.split("\n")
fichier_allowed_words.close()

fichier_possible_words = open("possible_words.txt","r")
possible_words = fichier_possible_words.read()
possible_words = possible_words.split("\n")
fichier_possible_words.close()

jaune = {1: None, 2: None, 3: None, 4: None, 5: None}
vert = {1: None, 2: None, 3: None, 4: None, 5: None}
gris = []

mot_solution = random.choice(possible_words)
def split(mot):
    return [lettre for lettre in mot]

#Fonctions d'info
mot_solution = split(mot_solution)
mots_outils = allowed_words.copy()
mots_solutions = possible_words.copy()
def info_1v1(mot_essai, mot_cible) :
    #Découpage des mots
    mot_essai_tranché = []
    for lettre in mot_essai :
        mot_essai_tranché.append(lettre)
    mot_cible_tranché = []
    for lettre in mot_cible :
        mot_cible_tranché.append(lettre)
    
    #Mise à jour des infos de couleur
    rang = 0
    jaune_temporaire = jaune.copy()
    gris_temporaire = gris.copy()
    vert_temporaire = vert.copy()
    for lettre in mot_essai_tranché :
        if lettre == mot_cible_tranché[rang] :
            vert_temporaire[rang+1] = lettre
        elif lettre not in mot_cible_tranché :
            gris_temporaire.append(lettre)
        else :
            jaune_temporaire[rang+1] = lettre
        rang = rang + 1
    #print("gris =",gris_temporaire, "vert =",vert_temporaire, "jaune=",jaune_temporaire)
    
    #Épuration des solutions possibles
    mots_solutions_temporaire = mots_solutions.copy()
    mots_exclus = []
    rang_liste = -1
    for mot in mots_solutions_temporaire :
        rang_lettre = 0
        rang_liste = rang_liste + 1
        for lettre in mot :
            if lettre in gris_temporaire :
                mots_exclus.append(mot)
                break
            elif vert_temporaire[rang_lettre+1] != lettre and vert_temporaire[rang_lettre+1] != None:
                mots_exclus.append(mot)
                break
            elif jaune_temporaire[rang_lettre+1]!= None : 
                if jaune_temporaire[rang_lettre+1] == lettre or jaune_temporaire[rang_lettre+1] not in split(mot) :
                    mots_exclus.append(mot)
                break
            rang_lettre = rang_lettre + 1
            if rang_lettre == 5 :
                rang_lettre = 0
                
    information_1v1 = len(mots_exclus)
    #print(mots_exclus)
    return(information_1v1)
    
def info_1vTotal(mot_essai, liste_mots_cible) :
    information_1vTotal = []
    for mot in liste_mots_cible :
        information_1vTotal.append(info_1v1(mot_essai, mot))
    information_1vTotal = stc.mean(information_1vTotal)
    return(information_1vTotal)

def info_maximale(liste_mots_outils, liste_mots_cible):
    repertoire_info = []
    passage = 0
    for mot in liste_mots_outils :
        passage = passage + 1
        print(passage)
        repertoire_info.append(info_1vTotal(mot, liste_mots_cible))
    information_maximale = max(repertoire_info)
    rang_info_max = repertoire_info.index(information_maximale)
    mot_optimal = allowed_words[rang_info_max]
    print(mot_optimal)
    return(mot_optimal)
#Processus d'un tour
def tour(mot_joué) :
    #Actualisation des infos de couleur
    rang = 0
    for lettre in split(mot_joué):
        if lettre == mot_solution[rang] :
            vert[rang+1] = lettre
        elif lettre not in mot_solution :
            gris.append(lettre)
        else :
            jaune[rang+1] = lettre
        rang = rang + 1
    print("gris =",gris)
    print("vert =",vert)
    print("jaune=",jaune)
    
    #Ecremage de la liste des mots possibles
    rang_liste = -1
    mots_exclus = []
    for mot in possible_words :
        rang_lettre = 0
        rang_liste = rang_liste + 1
        for lettre in mot :
            if lettre in gris :
                mots_exclus.append(mot)
                break
            elif vert[rang_lettre+1] != lettre and vert[rang_lettre+1] != None:
                mots_exclus.append(mot)
                break
            elif jaune[rang_lettre+1]!= None : 
                if jaune[rang_lettre+1] == lettre or jaune[rang_lettre+1] not in split(mot) :
                    mots_exclus.append(mot)
                break
            rang_lettre = rang_lettre + 1
            if rang_lettre == 5 :
                rang_lettre = 0
                
    for mot in mots_exclus :
        possible_words.remove(mot)
    print('Mots envisageables après ce tour : ',len(possible_words))
    global allowed_words
    allowed_words = possible_words
    print('Mode difficile : la liste de mots outils devient la même que celle des mots envisageables')
    #print('Autrement dit : ')
    #print(possible_words)
  
#Moyenne sur 2000 tests
liste_coups = [4,
 6,
 4,
 7,
 6,
 4,
 5,
 3,
 3,
 4,
 9,
 5,
 3,
 5,
 4,
 6,
 5,
 4,
 6,
 6,
 5,
 5,
 3,
 7,
 4,
 3,
 3,
 5,
 6,
 4,
 5,
 4,
 6,
 4,
 3,
 3,
 4,
 4,
 6,
 3,
 4,
 5,
 5,
 3,
 2,
 3,
 2,
 5,
 5,
 4,
 4,
 3,
 5,
 5,
 5,
 6,
 4,
 5,
 4,
 7,
 4,
 7,
 7,
 7,
 5,
 7,
 3,
 5,
 4,
 3,
 3,
 5,
 3,
 4,
 2,
 3,
 3,
 4,
 3,
 5,
 5,
 4,
 3,
 4,
 3,
 3,
 4,
 4,
 3,
 5,
 4,
 6,
 4,
 3,
 3,
 7,
 2,
 5,
 7,
 3,
 2]
moyenne_coups = 4.3861386138613865
nombre_de_tests = 101
for i in range(200) :
    nombre_de_tests = nombre_de_tests + 1
    print('Test numéro ', nombre_de_tests)
    #Initialisation
    fichier_allowed_words = open("allowed_words.txt","r")
    allowed_words = fichier_allowed_words.read()
    allowed_words = allowed_words.split("\n")
    fichier_allowed_words.close()

    fichier_possible_words = open("possible_words.txt","r")
    possible_words = fichier_possible_words.read()
    possible_words = possible_words.split("\n")
    fichier_possible_words.close()

    jaune = {1: None, 2: None, 3: None, 4: None, 5: None}
    vert = {1: None, 2: None, 3: None, 4: None, 5: None}
    gris = []

    mot_solution = random.choice(possible_words)
    #Élimination manuelle : utilisation de 'slier'
    tour('slier')
    compteur = 1
    #Suite normale
    while None in vert.values() :
        tour(info_maximale(allowed_words, possible_words))
        compteur = compteur + 1
    print('Le mot était ', str(possible_words), '.')
    print('Il a été trouvé en ', compteur,' coups.')
    liste_coups.append(compteur)
    moyenne_coups = stc.mean(liste_coups)
    print('Les jeux ont été résolus respectivement en :', liste_coups, ' tours.')
    print('La performance moyenne de la méthode est désormais de ', moyenne_coups, ' tours.')
    