#!/usr/bin/python
# -*-coding:Utf-8 -*

#---------------------------------------------------------------------

# SPLIT (=explode) :

ma_chaine = "Bonjour à tous"
print(ma_chaine.split(" "))
#['Bonjour', 'à', 'tous']

#---------------------------------------------------------------------

# JOIN (=implode) :

ma_liste = ['Bonjour', 'à', 'tous']
print(" ".join(ma_liste))
#'Bonjour à tous'

#---------------------------------------------------------------------

# FONCTION AVEC X PARAMS

def fonction_inconnue(*mes_params):
    """Test d'une fonction pouvant être appelée avec un nombre variable de paramètres"""
    print("J'ai reçu : {}.".format(mes_params))

fonction_inconnue() # On appelle la fonction sans paramètre
#J'ai reçu : ().

fonction_inconnue(33)
#J'ai reçu : (33,).

fonction_inconnue('a', 'e', 'f')
#J'ai reçu : ('a', 'e', 'f').

var = 3.5
fonction_inconnue(var, [4], "...")
#J'ai reçu : (3.5, [4], '...').

#---------------------------------------------------------------------

# LIST COMPREHESION
# Doc : https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/232143-les-listes-et-tuples-2-2

liste_origine = [0, 1, 2, 3, 4, 5]
print([nb * nb for nb in liste_origine])
#[0, 1, 4, 9, 16, 25]

liste_origine = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([nb for nb in liste_origine if nb % 2 == 0])
#[2, 4, 6, 8, 10]

qtt_a_retirer = 7 # On retire chaque semaine 7 fruits de chaque sorte
fruits_stockes = [15, 3, 18, 21] # Par exemple 15 pommes, 3 melons...
print([nb_fruits-qtt_a_retirer for nb_fruits in fruits_stockes if nb_fruits>qtt_a_retirer])
#[8, 11, 14]

#---------------------------------------------------------------------

inventaire = [
    ("pommes", 22),
    ("melons", 4),
    ("poires", 18),
    ("fraises", 76),
    ("prunes", 51),
]

# On change le sens de l'inventaire, la quantité avant le nom
inventaire_inverse = [(qtt, nom_fruit) for nom_fruit,qtt in inventaire]
# On n'a plus qu'à trier dans l'ordre décroissant l'inventaire inversé
# On reconstitue l'inventaire trié
inventaire = [(nom_fruit, qtt) for qtt,nom_fruit in sorted(inventaire_inverse, reverse=True)]
print(inventaire)

# On change le sens de l'inventaire, la quantité avant le nom
inventaire_inverse = [(qtt, nom_fruit) for nom_fruit,qtt in inventaire]
# On trie l'inventaire inversé dans l'ordre décroissant
inventaire_inverse.sort(reverse=True)
# Et on reconstitue l'inventaire
inventaire = [(nom_fruit, qtt) for qtt,nom_fruit in inventaire_inverse]
print(inventaire)

#---------------------------------------------------------------------

import pprint

pprint.pprint(globals())
print("\n\n\n")
pprint.pprint(locals())

#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------

input("Appuyez sur ENTREE pour fermer ce programme...")
