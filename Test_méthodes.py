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
import statistics


def test_iadebase(reps):
    liste_compteur=np.zeros(reps)
    liste_var=[]
    for i in range(reps):
        liste_var.append(m.wordle())
        liste_var[i].iadebaseshort()
        liste_compteur[i]=liste_var[i].compteur
    # print(liste_compteur)
    # print(sum(liste_compteur)/len(liste_compteur)) 
    
    # plt.hist(liste_compteur, align='left', facecolor='green', bins=range(1,17), rwidth=0.8)
    # plt.xticks(np.arange(0, 16))
    return liste_compteur
    
def test_iaesp_base(reps):
    liste_compteur=np.zeros(reps)
    liste_var=[]
    for i in range(reps):
        liste_var.append(m.wordle())
        liste_var[i].iaesp_base()
        liste_compteur[i]=liste_var[i].compteur
    # print(liste_compteur)
    # print(sum(liste_compteur)/len(liste_compteur)) 
    
    # plt.hist(liste_compteur, align='left', facecolor='green', bins=range(1,17), rwidth=0.8)
    # plt.xticks(np.arange(0, 16))
    return liste_compteur    

def test_iaesp_pos(reps):
    liste_compteur=np.zeros(reps)
    liste_var=[]
    for i in range(reps):
        liste_var.append(m.wordle())
        liste_var[i].iaesp_pos()
        liste_compteur[i]=liste_var[i].compteur
    # print(liste_compteur)
    # print(sum(liste_compteur)/len(liste_compteur)) 
    
    # plt.hist(liste_compteur, align='left', facecolor='green', bins=range(1,17), rwidth=0.8)
    # plt.xticks(np.arange(0, 16))  
    return liste_compteur 

def test_iteratif(reps):
    liste_compteur=np.zeros(reps)
    liste_var=[]
    for i in range(reps):
        liste_var.append(m.wordle())
        liste_var[i].iaelab()
        liste_compteur[i]=liste_var[i].compteur
    return liste_compteur 


def moyenne(liste):
    moyenne = sum(liste)/len(liste)
    return moyenne
    
liste_debase = test_iadebase(200)
liste_frequence = test_iaesp_base(200)
liste_frequence_pos = test_iaesp_pos(200)
liste_iteratif = test_iteratif(200)

moyenne_debase = moyenne(liste_debase)
moyenne_frequence = moyenne(liste_frequence)
moyenne_frequence_pos = moyenne(liste_frequence_pos)
moyenne_iteratif = moyenne(liste_iteratif)

fig = go.Figure()
fig.add_trace(go.Histogram(
    x=liste_debase,
    histnorm='percent',
    name='Témoin',
    marker_color='red',
    opacity=0.75
))
fig.add_trace(go.Histogram(
    x=liste_frequence,
    histnorm='percent',
    name='Algorithme fréquence',
    marker_color='blue',
    opacity=0.75
))
fig.add_trace(go.Histogram(
    x=liste_frequence_pos,
    histnorm='percent',
    name='Algorithme fréquence position',
    marker_color='cyan',
    opacity=0.75
))
fig.add_trace(go.Histogram(
    x=liste_iteratif,
    histnorm='percent',
    name='Algorithme itératif',
    marker_color='green',
    opacity=0.75
))

fig.update_layout(
    title_text='Distribution du nombre de coups par algorithme de résolution', 
    xaxis_title_text='Nombre de coups', 
    yaxis_title_text="Occurences", 
    bargap=0.2, 
    bargroupgap=0.1 
)

fig2 = go.Figure(data=[go.Table(header=dict(values=["",'Algorithme base', 'Algorithme fréquence', 'Algorithme fréquence position','Algorithme iteratif']),
                 cells=dict(values=[['Moyenne', 'Variance'],
                                    [moyenne_debase,statistics.variance(liste_debase)], 
                                    [moyenne_frequence,statistics.variance(liste_frequence)],
                                    [moyenne_frequence_pos,statistics.variance(liste_frequence_pos)],
                                    [moyenne_iteratif,statistics.variance(liste_iteratif)]]))
                       
                     ])
fig.show()
fig2.show()