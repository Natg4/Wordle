import numpy as np
#Préparation des listes de mots
#Mots autorisés
fichier_allowed_words = open("allowed_words.txt","r")
allowed_words = fichier_allowed_words.read()
allowed_words = allowed_words.split("\n")
fichier_allowed_words.close()
#Solutions envisageables
fichier_possible_words = open("possible_words.txt","r")
possible_words = fichier_possible_words.read()
possible_words = possible_words.split("\n")
fichier_possible_words.close()

tentatives_possibles = allowed_words.copy()
#Fonction de séparation des lettres d'un mot
def split(word):
    return [char for char in word]

#Listes
grey = []
yellow = [[],[],[],[],[]]
green = [[],[],[],[],[]]

#Fonction d'épuration
def epuration(tentatives_uno, liste_gris, liste_jaune, liste_vert):
    
    for i in range(len(liste_gris)):
        for j in reversed(range(len(tentatives_uno))):
            if liste_gris[i] in split(tentatives_uno[j]):
                tentatives_uno.pop(j)
    
    for i in range(len(liste_vert)):
        for j in reversed(range(len(tentatives_uno))):
            for u in range(len(split(liste_vert[i]))):
                if split(liste_vert[i])[u].isalpha():    
                    if liste_vert[i] != split(tentatives_uno[j])[i]:
                            tentatives_uno.pop(j)
    
    for i in range(len(liste_jaune)):
        for j in reversed(range(len(tentatives_uno))):
            for u in range(len(split(liste_jaune[i]))):
                if split(liste_jaune[i])[u].isalpha():    
                    if liste_jaune[i][u] == split(tentatives_uno[j])[i]:
                            tentatives_uno.pop(j)
                    elif liste_jaune[i][u] not in split(tentatives_uno[j]):
                            tentatives_uno.pop(j)
    return tentatives_uno

jaune = yellow.copy()
vert = green.copy()
gris = grey.copy()         
def actualisation_couleurs(mot_test, mot_choisi):

    for i in range(len(mot_test)):
        if mot_test[i] in mot_choisi and mot_test[i] != mot_choisi[i] :
            if not(mot_test[i] in yellow):
                jaune[i].append(mot_test[i])
                        
                        
            elif mot_test[i] == mot_choisi[i] :
                vert[i] = mot_test[i]
                        
            else : 
                gris.append(mot_test[i])
    

def info_post_test(mot_essai,mot_cible):
    taille_initiale = len(tentatives_possibles)
    actualisation_couleurs(mot_essai,mot_cible)
    copie = tentatives_possibles.copy()
    taille_post_test = len(epuration(copie, gris, jaune, vert))
    info_post_test = taille_post_test/taille_initiale
    return info_post_test
    
def information_solo(mot_essai, mots_possibles_actuellement):
    info = np.array(len(mots_possibles_actuellement))
    for mot in mots_possibles_actuellement :
        np.append(info, info_post_test(mot, mots_possibles_actuellement)/len(mots_possibles_actuellement))
    info = info.mean()
    return info
    
def grosse_info(mots_autorises, mots_possibles_actuellement):
    maxi_info = np.array
    for mot in mots_autorises :
        np.append(maxi_info)
    maxi_info = maxi_info.mean()
    return maxi_info