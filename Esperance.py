# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 21:49:41 2022

@author: natha
"""
import fonction as fo
import string
import numpy as np
import statistics as stc



Alphabet=list(string.ascii_lowercase)






class vecesp():
    def __init__(self,possible):
        self.vecnbr=np.zeros(26)
        self.vecfreq=np.zeros(26)
        self.possibilite=possible
        self.vecnbr_pos=np.zeros(shape=5*26).reshape(26,5)
        self.vecfreq_pos=np.zeros(shape=5*26).reshape(26,5)
    
    def comptagedelettre(self):
        listesplite=fo.split(list("".join(self.possibilite)))
        for i in range(26):
            self.vecnbr[i]=listesplite.count(Alphabet[i])
        self.vecfreq=self.vecnbr/len("".join(self.possibilite))
        
    def espdeliste(self):
            self.comptagedelettre()
            dico = dict(zip(range(ord('a'),ord('z')+1), self.vecfreq))
            meilleur_score=0
            meilleur_element='rien'
            for element in self.possibilite:
                score=0
                for char in list(element):
                    if list(element).count(char)==1:
                        score=score+float(dico[ord(char)])
                        
                if score>meilleur_score:
                    meilleur_score=score
                    meilleur_element=element
                    print(score)
            return meilleur_element
    
    def comptagedelettre_pos(self):
        for element in list(self.possibilite):
            mot=list(element)
            for i in range(len(mot)):
                for char in Alphabet:
                    if mot[i]==char:
                        self.vecnbr_pos[ord(char)-97,i]+=1
                        
        self.vecfreq_pos=self.vecnbr_pos/len(self.possibilite)
        
    def espdeliste_pos(self):
        self.comptagedelettre_pos()
        dico=[{}]*5
        for i in range(5):
            dico[i]=dict(zip(range(ord('a'),ord('z')+1),self.vecfreq_pos[:,i]))
        meilleur_score=0
        meilleur_element='rien'
        for element in self.possibilite:
            score=0
            for i in range(5):
                score=score+float(dico[i][ord(list(element)[i])])
            if score>=meilleur_score:
                meilleur_score=score
                meilleur_element=element
                print(score)
                print(meilleur_element)
        return meilleur_element
            
            
            
        
def info_1v1(mot_essai, mot_cible,mots_solutions) :
    
    
    jaune = {1: None, 2: None, 3: None, 4: None, 5: None}
    vert = {1: None, 2: None, 3: None, 4: None, 5: None}
    gris = []
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
    mots_solutions_temporaire = list(mots_solutions)
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
                if jaune_temporaire[rang_lettre+1] == lettre or jaune_temporaire[rang_lettre+1] not in fo.split(mot) :
                    mots_exclus.append(mot)
                break
            rang_lettre = rang_lettre + 1
            if rang_lettre == 5 :
                rang_lettre = 0
                
    information_1v1 = len(mots_exclus)
    #print(mots_exclus)
    return(information_1v1)
    
def info_1vTotal(mot_essai, liste_mots_cible,mots_solutions) :
    information_1vTotal = []
    for mot in liste_mots_cible :
        information_1vTotal.append(info_1v1(mot_essai, mot,mots_solutions))
    information_1vTotal = stc.mean(information_1vTotal)
    return(information_1vTotal)

def info_maximale(liste_mots_outils, liste_mots_cible,mots_solutions):
    repertoire_info = []
    passage = 0
    for mot in liste_mots_outils :
        passage = passage + 1
        print(passage)
        repertoire_info.append(info_1vTotal(mot, liste_mots_cible,mots_solutions))
    information_maximale = max(repertoire_info)
    rang_info_max = repertoire_info.index(information_maximale)
    mot_optimal = liste_mots_outils[rang_info_max]
    print(mot_optimal)
    return(mot_optimal)


                
            
                    
        

