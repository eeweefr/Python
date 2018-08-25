#!/usr/bin/python
# -*-coding:Utf-8 -*

# Sous Windows (utiliser os.system("pause"), pour faire une pause dans l'exec du prog)
#import os # On importe le module os
print("Bonjour le monde !")
#os.system("pause")



# FOR :
#print("\n");
#mot = "toto et titi"
#for lettre in mot:
#    print(lettre," --- ",len(mot))




# IF, ELSE :
#print("\n");
#if "T" in "Taefkjb":
#    print("T trouvé dans la chaine.");
#else :
#    print("T non trouvé");




# FUNCTION :
# DOCSTRING > help(nom_de_votre_fonction) : permettra d'afficher le texte entre """ici""".
print("\n");
def table(nb, max=3):
    """Fonction affichant la table de multiplication par nb
    de 1*nb à max*nb

    (max >= 0)"""
    i = 0
    while i < max: # Tant que i est strictement inférieure à 10,
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1 # On incrémente i de 1 à chaque tour de boucle.

#table(5)
#help(table)




# FUNCTION : lambda
print("\n");
a = lambda x: print(x * x)
a(4)

b = lambda x,y: print(x + y)
b(4,2)




# MODULE : math
print("\n");
import math
# ou
# import math as mathematiques
racine_de_x = math.sqrt(16)
print(racine_de_x)

# Obtenir la doc d'une class
#help("math")
#help("math.sqrt")




# FROM : ajouter fabs uniquement (accessible en global par un fabs)
print("\n");
#Note fabs : renvoyer la valeur absolue d'un chiffre
"""
from math import fabs
print( fabs(-5) )
print( fabs(2) )
"""

"""Importer tout dans l'espace de nom principal"""
from math import *
print( fabs(-5) )








def afficher_flottant(flottant):
    """Fonction prenant en paramètre un flottant et renvoyant une chaîne de caractères représentant la troncature de
    ce nombre. La partie flottante doit avoir une longueur maximum de 3 caractères.

    De plus, on va remplacer le point décimal par la virgule"""

    if type(flottant) is not float:
        raise TypeError("Le paramètre attendu doit être un flottant")
    flottant = str(flottant)
    partie_entiere, partie_flottante = flottant.split(".")
    # La partie entière n'est pas à modifier
    # Seule la partie flottante doit être tronquée
    return ",".join([partie_entiere, partie_flottante[:3]])

print("float : ",afficher_flottant(3.34567890876543))
print("float : ",afficher_flottant(1.6))







# Sous Linux / Mac (utiliser un input)
print("\n");
input("Appuyez sur ENTREE pour fermer ce programme...")
