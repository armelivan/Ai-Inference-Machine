class Recherche:
    """ Classe générique pour la recherche. """

    echec = 'échec'

    def __init__(self):
        """

        """

    def recherche_chemin(self, noeud_depart):
        """ Recherche les  chemin allant de ``depart``  aux noeuds terminaux.

            :param noeud_depart: le noeud de départ.

            :return: les  differents chemins
        """
        queue = [(noeud_depart, [])]  # [(noeud,[(parent1,valeur1),(parent2,valeur2)...])]
        chemins = []
        iterations = 0

        while len(queue) > 0:

            # print( str(len(queue))+'\n' )

            noeud = queue.pop(0)
            iterations += 1
            # print('itération # :'+ str(iterations)+'\n')

            if noeud[0].attribut == None:  # si on a un noeud terminal
                chemins.append(noeud[1])  # On retourne la liste de tuple constituant son chemin

            else:

                successeurs = self.trouve_successeurs(noeud[0], noeud[1])
                queue = self.ajoute_successeurs(queue, successeurs)
        chemins_modified = []

        #  Retourne les élements sous le formats des règles
        for chemin in chemins:
            tab = []

            target = chemin[len(chemin) - 1][1]
            for item in chemin:
                tab.append(item[0])
            chemins_modified.append([tab, target])

        return chemins_modified

    def trouve_successeurs(self, noeud, parentList):
        """ Trouve les successeurs du noeud courant.

            :return: une liste contenant les noeuds successeurs du noeud courant.
        """
        successeurs = []

        # print('parentList: '+str(parentList))

        # pour chaque element on cherche a ajouter les prochain
        for key in noeud.enfants:
            # print( '    valeur' +str(key))
            parent = parentList.copy()
            parent.append((noeud.attribut + "-" + key, noeud.donnees[0][0]))
            # print('     parent:'+str(parent))
            successeurs.append((noeud.enfants[key], parent))

        return successeurs

    def ajoute_successeurs(self, queue, successeurs):
        """
        :param queue:
        :param successeurs:
        :return: une nouvelle structure composée des deux précédentes
        """

        if len(queue) == 0:
            return successeurs
        return queue + successeurs
