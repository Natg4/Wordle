#python 3
# UTF8

"""
doumentation du module
Docstring = ce que fait notre programme
"""
import random
import plotly.graph_objects as go
import plotly.io as pio
import fonction as f
import Esperance as es
import string
import numpy as np
Alphabet=list(string.ascii_lowercase)
pio.renderers.default='browser'

fichier_allowed_words = open("allowed_words.txt","r")
allowed_words = fichier_allowed_words.read()
allowed_words = allowed_words.split("\n")
fichier_allowed_words.close()

fichier_possible_words = open("possible_words.txt","r")
possible_words = fichier_possible_words.read()
possible_words = possible_words.split("\n")
fichier_possible_words.close()


class wordle:
    def __init__(self):
         self.possible=list(allowed_words)
         self.autorise=list(possible_words)
         self.mot=random.choice(allowed_words)
         self.grey=[]
         self.green=[0]*5
         self.yellow=f.creation_liste(self.mot)
         self.compteur=0
   
    def jouer(self):
        tentative=[]
        
        while tentative != self.mot:
            tentative=f.split(f.fonction_mot_test())
        
            for i in range(len(tentative)):
                if tentative[i] in self.mot and tentative[i] != self.mot[i] :
                    if not(tentative[i] in self.yellow[i]):
                            self.yellow[i].append(tentative[i])
                            
                    
                    
                elif tentative[i] == self.mot[i] :
                        self.green[i] = tentative[i]
                        
                    
                else : 
                    if tentative[i] not in self.grey:
                        self.grey.append(tentative[i])
                        
            if self.green != f.split(self.mot) :
                print("Green list :",self.green)
                print("Grey list:",self.grey)
                print("Yellow list:",self.yellow)
        
            else :
                print("Bravo !")
                break
            
    def tri(self, tentative):
    
        for i in range(len(self.grey)):
            for j in reversed(range(len(self.possible))):
                if self.grey[i] in f.split(self.possible[j]):
                    self.possible.pop(j)
    
        for i in range(len(self.green)):
            if self.green[i] in Alphabet:
                for j in reversed(range(len(self.possible))):
                    if self.green[i] != self.possible[j][i]:
                        self.possible.pop(j)
     
        for i in range(len(self.yellow)):
            for j in reversed(range(len(self.possible))):
                for u in range(len(f.split(self.yellow[i]))):
                    if f.split(self.yellow[i])[u].isalpha():    
                        if self.yellow[i][u] == f.split(self.possible[j])[i]:
                            self.possible.pop(j)
                    elif self.yellow[i][u] not in f.split(self.possible[j]):
                            self.possible.pop(j)
                        
    
    def essai(self,essai):
        for i in range(len(essai)):
            if essai[i] in self.mot and essai[i] != self.mot[i] :
                if not(essai[i] in self.yellow[i]):
                        self.yellow[i].append(essai[i])
                        
                
                
            elif essai[i] == self.mot[i] :
                    self.green[i] = essai[i]
                    
                
            else : 
                    self.grey.append(essai[i])
    
    def iadebase(self):
        
        essai=[]
        self.compteur=0
        self.possible=list(allowed_words)
        while essai != self.mot :
            essai=random.choice(self.possible)
            
            self.essai(essai)
                        
            if self.green != f.split(self.mot) :
                print("Mot tenté:",essai)
                print("Green list :",self.green)
                print("Grey list:",self.grey)
                print("Yellow list:",self.yellow)
                
                self.compteur+=1
                self.tri(essai)
                print(self.possible)
        
            else :
                print("Bravo !")
                print("La réponse était:",self.mot)
                print("Compteur=",self.compteur)
                break
            
    def iadebaseshort(self):
            essai=[]
            self.compteur=0
            self.possible=list(allowed_words)
            while essai != self.mot :
                essai=random.choice(self.possible)
                self.compteur+=1
                self.essai(essai)
                            
                if self.green != f.split(self.mot) :
                    self.tri(essai)
            
                else :
                    break

    def iaesp_base(self):
        essai=[]
        self.compteur=0
        self.possible=list(allowed_words)
        while essai != self.mot :
                possibilite=es.vecesp(self.possible)
                essai=possibilite.espdeliste()
                self.compteur+=1
                self.essai(essai)
                
                if self.green != f.split(self.mot):
                    self.tri(essai)
                else:
                    print("Mot :",self.mot," trouvé en ",self.compteur)



    def iaesp_pos(self):
        essai=[]
        self.compteur=0
        self.possible=list(allowed_words)
        while essai != self.mot :
                possibilite=es.vecesp(self.possible)
                essai=possibilite.espdeliste_pos()
                self.compteur+=1
                self.essai(essai)
                
                if self.green != f.split(self.mot):
                    self.tri(essai)
                else:
                    print("Mot :",self.mot," trouvé en ",self.compteur)
    


        

            
        
        
         
         

         
         

         


         

