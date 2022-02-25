#!/usr/bin/env python
# coding: utf-8
from id3.moteur_id3.noeud_de_decision import NoeudDeDecision
from id3.moteur_id3.id3 import ID3


def traiter_donnees(nom_fichier):
    f = open(nom_fichier, "r", encoding='utf-8-sig')
    
    premiereLigne = f.readline()
    
    noms_attributs = premiereLigne.split(',')
    noms_attributs = [nom_attribut.strip() for nom_attribut in noms_attributs]
    
    donnees = []
    
    ligne = f.readline()
    while ligne !='':
        attributs = ligne.split(',')
        donnee = [attributs[-1][0], {}]
        for index_col in range(0, len(attributs)-1):
            donnee[1].update({noms_attributs[index_col] : attributs[index_col]})
        
        donnees.append(donnee)
        ligne = f.readline()

    return donnees
   
    
def calculer_precision(arbre, donnees_test):
    count_ok = 0
    
    for donnee in donnees_test:
        res = arbre.classifie(donnee[1])[1]
        if(res == donnee[0]):
            count_ok += 1
            
    return count_ok*100 / len(donnees_test)




