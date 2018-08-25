#!/usr/bin/python
# -*-coding:Utf-8 -*

#---------------------------------------------------------------------
# SOURCE : https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/232273-les-dictionnaires
#
# dictionnaire = {cle1:valeur1, cle2:valeur2, cleN:valeurN}
# dictionnaire[cle] = valeur
#
# keys, values, items
#---------------------------------------------------------------------

# LES DICTIONNAIRES :

mon_dictionnaire = dict()
print(type(mon_dictionnaire))
#<class 'dict'>
print(mon_dictionnaire)
#{}

# ou
mon_dictionnaire = {}
print(mon_dictionnaire)
#{}

#---------------------------------------------------------------------

mon_dictionnaire = {}
mon_dictionnaire["pseudo"] = "Prolixe"
mon_dictionnaire["mot de passe"] = "*"
print(mon_dictionnaire)
#{'mot de passe': '*', 'pseudo': 'Prolixe'}

#---------------------------------------------------------------------

mon_dictionnaire = {}
mon_dictionnaire["pseudo"] = "Prolixe"
mon_dictionnaire["mot de passe"] = "*"
mon_dictionnaire["pseudo"] = "6pri1"
print(mon_dictionnaire)
#{'mot de passe': '*', 'pseudo': '6pri1'}

#---------------------------------------------------------------------

mon_dictionnaire = {}
mon_dictionnaire[0] = "a"
mon_dictionnaire[1] = "e"
mon_dictionnaire[2] = "i"
mon_dictionnaire[3] = "o"
mon_dictionnaire[4] = "u"
mon_dictionnaire[5] = "y"
print(mon_dictionnaire)
#{0: 'a', 1: 'e', 2: 'i', 3: 'o', 4: 'u', 5: 'y'}

#---------------------------------------------------------------------

echiquier = {}
echiquier['a', 1] = "tour blanche" # En bas à gauche de l'échiquier
echiquier['b', 1] = "cavalier blanc" # À droite de la tour
echiquier['c', 1] = "fou blanc" # À droite du cavalier
echiquier['d', 1] = "reine blanche" # À droite du fou
# ... Première ligne des blancs
echiquier['a', 2] = "pion blanc" # Devant la tour
echiquier['b', 2] = "pion blanc" # Devant le cavalier, à droite du pion
# ... Seconde ligne des blancs

#---------------------------------------------------------------------

placard = {"chemise":3, "pantalon":6, "tee-shirt":7}

#---------------------------------------------------------------------

# DELETE

placard = {"chemise":3, "pantalon":6, "tee shirt":7}
del placard["chemise"]
print(placard)

placard = {"chemise":3, "pantalon":6, "tee shirt":7}
print(placard.pop("chemise"))
print(placard)
#3

#---------------------------------------------------------------------

fruits = {"pommes":21, "melons":3, "poires":31}
for v in fruits:
    print(v)

#melons
#poires
#pommes

#---------------------------------------------------------------------

# KEYS

fruits = {"pommes":21, "melons":3, "poires":31}
for cle in fruits.keys():
    print(cle)
#melons
#poires
#pommes

#---------------------------------------------------------------------

# VALUES

fruits = {"pommes":21, "melons":3, "poires":31}
for valeur in fruits.values():
    print(valeur)

#3
#31
#21

#---------------------------------------------------------------------

if 21 in fruits.values():
    print("Un des fruits se trouve dans la quantité 21.")

#Un des fruits se trouve dans la quantité 21.

#---------------------------------------------------------------------

# ITEMS (= key / value)

fruits = {"pommes":21, "melons":3, "poires":31}
for cle, valeur in fruits.items():
    print("La clé {} contient la valeur {}.".format(cle, valeur))

#La clé melons contient la valeur 3.
#La clé poires contient la valeur 31.
#La clé pommes contient la valeur 21.

#---------------------------------------------------------------------

# def fonction_inconnue(*en_liste, **en_dictionnaire):
# Tous les paramètres non nommés se retrouveront dans la variableen_listeet les paramètres nommés dans la variableen_dictionnaire.

def fonction_inconnue(**parametres_nommes):
    """Fonction permettant de voir comment récupérer les paramètres nommés
    dans un dictionnaire"""


    print("J'ai reçu en paramètres nommés : {}.".format(parametres_nommes))

fonction_inconnue() # Aucun paramètre
#J'ai reçu en paramètres nommés : {}
fonction_inconnue(p=4, j=8)
#J'ai reçu en paramètres nommés : {'p': 4, 'j': 8}

#---------------------------------------------------------------------

parametres = {"sep":" >> ", "end":" -\n"}
print("Voici", "un", "exemple", "d'appel", **parametres)
#Voici >> un >> exemple >> d'appel -

# Equivalent

print("Voici", "un", "exemple", "d'appel", sep=" >> ", end=" -\n")
#Voici >> un >> exemple >> d'appel -

#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------

input("Appuyez sur ENTREE pour fermer ce programme...")
