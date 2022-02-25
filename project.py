from helpers import *
from id3.moteur_id3.noeud_de_decision import NoeudDeDecision
from id3.moteur_id3.id3 import ID3
from recherche.recherche import Recherche
from moteur_sans_variables.connaissance import BaseConnaissances
from moteur_sans_variables.regle_sans_variables import RegleSansVariables
from moteur_sans_variables.chainage_avant_sans_variables import ChainageAvantSansVariables



class ResultValues():

    def __init__(self):
        
        #Traitement
        donnees = traiter_donnees("data/train_bin.csv") #reformatter les donnees pour le modèle utilisé pour construire l'arbre
        id3 = ID3()
        
        # Task 1
        self.arbre = id3.construit_arbre(donnees)
        
        # Task 3
        self.faits_initiaux = donnees
        self.regles = None
        
        # Task 5
        self.arbre_advance = None

    def get_results(self):
        return [self.arbre, self.faits_initiaux, self.regles, self.arbre_advance]

    # retourne la règle justificative pour un lot d'exemples
    def explain_results(self, regles, donnees):
        List_el = []
        for donnee in donnees:
            List_el.append(self.explain_result(regles, donnee))
        return List_el

    # retourne la règle justificatif pour un exemple
    def explain_result(self, regles, donnee):

        fait = []
        for key in donnee[1]:
            fait.append(key + '-' + donnee[1][key])

        bc = BaseConnaissances(lambda descr: RegleSansVariables(descr[0], descr[1]))
        bc.ajoute_faits(fait)
        bc.ajoute_regles(regles)
        moteur = ChainageAvantSansVariables(bc)

        return moteur.chaine()


resultats = ResultValues().get_results()

#Task 1
print('Arbre de décision :')

print(resultats[0])

infos_arbre = resultats[0].infos_arbre()

print('Taille maximale des chemins :' + str(infos_arbre[0]) + '\n')

print('Taille moyenne des chemins :' + str(infos_arbre[1]) + '\n')


#Task 2
donnees_test = traiter_donnees("data/test_public_bin.csv")

print('Précision des prédictions :' + str(calculer_precision(resultats[0], donnees_test)) + '%' + '\n')



#Task 3
tosearch = Recherche()
regles = tosearch.recherche_chemin(resultats[0])
explication = ResultValues().explain_results(regles, donnees_test)

iteration = 1
for val in explication:
    print(str(iteration) + ")" + str(val))
    iteration += 1
