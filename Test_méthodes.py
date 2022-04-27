# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 21:45:44 2022

@author: natha
"""

import random
import plotly.graph_objects as go
import plotly.io as pio
import fonction as f
import Esperance
import string
import numpy as np
import main as m
import matplotlib.pyplot as plt
import seaborn as sns

def test_iadebase(reps):
    liste_compteur=np.zeros(reps)
    liste_var=[]
    for i in range(reps):
        liste_var.append(m.wordle())
        liste_var[i].iadebaseshort()
        liste_compteur[i]=liste_var[i].compteur
    print(liste_compteur)
    print(sum(liste_compteur)/len(liste_compteur)) 
    
    plt.hist(liste_compteur, align='left', facecolor='green', bins=range(1,17), rwidth=0.8)
    plt.xticks(np.arange(0, 16))
    
def test_iaesp_base(reps):
    liste_compteur=np.zeros(reps)
    liste_var=[]
    for i in range(reps):
        liste_var.append(m.wordle())
        liste_var[i].iaesp_base()
        liste_compteur[i]=liste_var[i].compteur
    print(liste_compteur)
    print(sum(liste_compteur)/len(liste_compteur)) 
    
    plt.hist(liste_compteur, align='left', facecolor='green', bins=range(1,17), rwidth=0.8)
    plt.xticks(np.arange(0, 16))    

def test_iaesp_pos(reps):
    liste_compteur=np.zeros(reps)
    liste_var=[]
    for i in range(reps):
        liste_var.append(m.wordle())
        liste_var[i].iaesp_pos()
        liste_compteur[i]=liste_var[i].compteur
    print(liste_compteur)
    print(sum(liste_compteur)/len(liste_compteur)) 
    
    plt.hist(liste_compteur, align='left', facecolor='green', bins=range(1,17), rwidth=0.8)
    plt.xticks(np.arange(0, 16))  

plt.show()
test_iaesp_pos(20)        
        