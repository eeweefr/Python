#!/usr/bin/python
# -*-coding:Utf-8 -*

#---------------------------------------------------------------------

mon_string = str() # On crée une liste vide
print("type: ")
print(type(mon_string))
#<class 'list'>
print(mon_string)

#---------------------------------------------------------------------

# lower :

aaa = "TEST POUR VOIR"
aaa = aaa.lower()
print( aaa )
print( type( aaa ) )

#---------------------------------------------------------------------

"""
chaine = str() # Crée une chaîne vide
# On aurait obtenu le même résultat en tapant chaine = ""

while chaine.lower() != "q":
    print("Tapez 'Q' pour quitter...")
    chaine = input()

print("Merci !")
"""

#---------------------------------------------------------------------

# upper, capitalize, strip, center

minuscules = "une chaine en minuscules"
print(minuscules.upper()) # Mettre en majuscules
#'UNE CHAINE EN MINUSCULES'

print(minuscules.capitalize()) # La première lettre en majuscule
#'Une chaine en minuscules'

espaces = "   une  chaine avec  des espaces   "
print(espaces.strip()) # On retire les espaces au début et à la fin de la chaîne
#'une  chaine avec  des espaces'

titre = "introduction"
print(titre.upper().center(20))
#'    INTRODUCTION    '

#---------------------------------------------------------------------

help( str )

#---------------------------------------------------------------------

# format

prenom = "Paul"
nom = "Dupont"
age = 21
print("Je m'appelle {0} {1} et j'ai {2} ans.".format(prenom, nom, age))
#Je m'appelle Paul Dupont et j'ai 21 ans.

# ou
nouvelle_chaine = "Je m'appelle {0} {1} et j'ai {2} ans.".format(prenom, nom, age)
print( nouvelle_chaine )

# ou
prenom = "Paul"
nom = "Dupont"
age = 21
print( \
    "Je m'appelle {0} {1} ({3} {0} pour l'administration) et j'ai {2} " \
    "ans.".format(prenom, nom, age, nom.upper()))
#Je m'appelle Paul Dupont (DUPONT Paul pour l'administration) et j'ai 21 ans.

#---------------------------------------------------------------------

date = "Dimanche 24 juillet 2011"
heure = "17:00"
print("Cela s'est produit le {}, à {}.".format(date, heure))
#Cela s'est produit le Dimanche 24 juillet 2011, à 17:00.

#---------------------------------------------------------------------

# formatage d'une adresse
adresse = """
{no_rue}, {nom_rue}
 {code_postal} {nom_ville} ({pays})
""".format(no_rue=5, nom_rue="rue des Postes", code_postal=75003, nom_ville="Paris", pays="France")
print(adresse)

#---------------------------------------------------------------------

prenom = "Paul"
message = "Bonjour"
chaine_complete = message + prenom # On utilise le symbole '+' pour concaténer deux chaînes
print(chaine_complete) # Résultat :
#BonjourPaul

# Pas encore parfait, il manque un espace
# Qu'à cela ne tienne !
chaine_complete = message + " " + prenom
print(chaine_complete) # Résultat :
#Bonjour Paul

#---------------------------------------------------------------------

"""
age = 21
message = "J'ai " + age + " ans."
print(message)
"""
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: Can't convert 'int' object to str implicitly

#---------------------------------------------------------------------

age = 21
message = "J'ai " + str(age) + " ans."
print(message)
#J'ai 21 ans.

#---------------------------------------------------------------------

chaine = "Salut les ZER0S !"

print(chaine[0]) # Première lettre de la chaîne
'S'

print(chaine[2]) # Troisième lettre de la chaîne
#'l'

print(chaine[-1]) # Dernière lettre de la chaîne
#'!'

#---------------------------------------------------------------------

chaine = "Salut"
print(len(chaine))
print(chaine.__len__())
#5

#---------------------------------------------------------------------

chaine = "Salut"
i = 0 # On appelle l'indice 'i' par convention
while i < len(chaine):
    print(chaine[i]) # On affiche le caractère à chaque tour de boucle
    i += 1

#---------------------------------------------------------------------

# INTERDIT :
"""
mot = "lac"
mot[0] = "b" # On veut remplacer 'l' par 'b'
"""
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: 'str' object does not support item assignment

#---------------------------------------------------------------------

# chaine[indice_debut:indice_fin]

presentation = "salut"
print(presentation[0:2]) # On sélectionne les deux premières lettres
#'sa'

print(presentation[2:len(presentation)]) # On sélectionne la chaîne sauf les deux premières lettres
#'lut'

#---------------------------------------------------------------------

print(presentation[:2]) # Du début jusqu'à la troisième lettre non comprise
#'sa'

print(presentation[2:]) # De la troisième lettre (comprise) à la fin
#'lut'

#---------------------------------------------------------------------

mot = "lac"
mot = "b" + mot[1:]
print(mot)
#bac

#---------------------------------------------------------------------



#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------

input("Appuyez sur ENTREE pour fermer ce programme...")
