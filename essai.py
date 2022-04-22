#python 3
# UTF8

"""
doumentation du module
Docstring = ce que fait notre programme
"""
import random
import plotly.graph_objects as go
import plotly.io as pio
import fonction

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
         self.possible=allowed_words
         self.autorise=possible_words
         self.mot=random.choice(allowed_words)
         self.grey=[]
         self.green=[0]*5
         self.yellow=creation_liste(self.mot)
   
    def jouer(self):
        tentative=[]
        
        while tentative != self.mot:
            tentative=split(fonction_mot_test())
        
            for i in range(len(tentative)):
                if tentative[i] in self.mot and tentative[i] != self.mot[i] :
                    if not(tentative[i] in self.yellow[i]):
                            self.yellow[i].append(tentative[i])
                            
                    
                    
                elif tentative[i] == self.mot[i] :
                        self.green[i] = tentative[i]
                        
                    
                else : 
                        self.grey.append(tentative[i])
                        
            if self.green != split(self.mot) :
                print("Green list :",self.green)
                print("Grey list:",self.grey)
                print("Yellow list:",self.yellow)
        
            else :
                print("Bravo !")
                break
                        
test=wordle()
test.jouer()
            
        
        
         
         

         
         

         


         

