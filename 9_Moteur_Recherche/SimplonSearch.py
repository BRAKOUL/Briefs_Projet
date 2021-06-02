# -*- coding: utf-8 -*-
"""
Created on Mon May 17 14:24:45 2021

@author: rlach
"""

from re import *
import os

recherche = "analyse et visualisation"
dossier_de_recherche = 'Jeux_de_donnees/textes'

# 1.

def almost(mot, s):
    z = " "+sub("[.,]", "", s)+" "
    found = findall("\s"+mot+"\s", z)
    for i in range(len(mot)):
        motif = "\s"+mot[:i]+mot[i+1:]+"\s"
        found += findall(motif, " "+z)
    return found

# 2.

def pluslarge(mot, s):
    z = " "+sub("[,.]", "", s)+ " "
    found = findall("\s"+mot+"[^\s]?\s", z)
    for i in range(len(mot)):
        # Je cherche le mot avec une lettre remplacé
        motif = "\s"+mot[:i]+"[^"+mot[i]+"]?"
        motif += mot[i+1:]+"\s"
        found += findall(motif, " "+z)
        # Je cherche le mot avec une lettre en plus
        motif += "\s"+mot[:i]+"[^\s]"+mot[i:]+"\s"
        found += findall(motif, " "+z)
    return found

# 3.

def score(p, s):
    sc = 0
    q = " "+sub("[,.]","", p)+" "
    z = " " + sub("[,.]","", s)
    for x in p.split():
        sc += len(pluslarge(x, s))
        sc += 4*z.count(" "+x+" ")
    return sc

def score2(p, s):
    s = s.lower()
    p = p.lower()
    sc = 0
    q = " "+sub("[,.]", "", p)+ " "
    z = " "+sub("[,.]", "", s)+ " "
    mots = p.split()
    for x in mots:
        for y in pluslarge(x, z):
            sc += 5 if y in q else 1
    for i in range(len(mots)-1):
        if " "+mots[i]+" "+mots[i+1]+" " in z :
            sc += 20
    return sc

liste = os.listdir(dossier_de_recherche)
results={}



for file in liste:
    filin = open("Jeux_de_donnees/textes/"+file, "r", encoding="utf-8")
    filin = filin.read()
    results[file] = score2(recherche, filin)
    
tuples = sorted(results.items(), key=lambda item: item[1], reverse=True)

for i, j in tuples :
    print(i + " : " + str(j))