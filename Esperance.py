# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 21:49:41 2022

@author: natha
"""
import fonction as fo
import string
import numpy as np

fichier_possible_words = open("possible_words.txt","r")
possible_words = fichier_possible_words.read()
possible_words=possible_words.split("\n")
fichier_possible_words.close()
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
            
            
            
        

                
            
                    
        
test=vecesp(possible_words)
print(test.espdeliste_pos())
