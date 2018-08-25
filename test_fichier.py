#!/usr/bin/python
# -*-coding:Utf-8 -*

#---------------------------------------------------------------------
# SOURCE : https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/232431-les-fichiers
#
# 'r': ouverture en lecture (Read).
# 'w': ouverture en écriture (Write). Le contenu du fichier est écrasé. Si le fichier n'existe pas, il est créé.
# 'a': ouverture en écriture en mode ajout (Append). On écrit à la fin du fichier sans écraser l'ancien contenu du
#      fichier. Si le fichier n'existe pas, il est créé.
#
# Pickle (save objet dans fichier).
#---------------------------------------------------------------------

import os
print("Repertoire courant (CWD=Current Working Directory) : ",os.getcwd())
print("Changement de repertoire courant.")
os.chdir("/Users/michaeldumontet/Documents/python/projet_a/test_fichier")
print("Repertoire courant (CWD=Current Working Directory) : ",os.getcwd())

#---------------------------------------------------------------------

help(os)

#---------------------------------------------------------------------

mon_fichier = open("fichier.txt", "r")
print(mon_fichier)
#<_io.TextIOWrapper name='fichier.txt' encoding='cp1252'>
print(type(mon_fichier))
#<class '_io.TextIOWrapper'>
mon_fichier.close()

#---------------------------------------------------------------------

# LIRE LE .TXT

mon_fichier = open("fichier.txt", "r")
contenu = mon_fichier.read()
print("Contenu du fichier .txt : ",contenu)
#C'est le contenu du fichier. Spectaculaire non ?
mon_fichier.close()

print("----")

#---------------------------------------------------------------------

# Syntaxe à utiliser si on ne fait qu'un open (sans le with).
# Car le fichier sera toujours fermé, grâce à "finally"
# NB : avec "with", le fichier est fermé automatiquement.

fichier = open("fichier.txt", "r")
try:
    # manipulation du fichier
finally:
    fichier.close()

print("----")

#---------------------------------------------------------------------

# ECRIRE DANS LE .TXT

"""
mon_fichier = open("fichier.txt", "a")
mon_fichier.write("Premier test d'écriture dans un fichier via Python")
mon_fichier.close()
"""

#---------------------------------------------------------------------

with open('fichier.txt', 'r') as mon_fichier:
    texte = mon_fichier.read()
    print("\nRendu du fichier .txt : ",texte)

# Check si le fichier est fermé
if mon_fichier.closed == True:
    print("--- Fichier fermé ---")
else:
    print("--- Fichier non fermé ---")

print("----")

#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------

# PICKLE : save de la data dans un fichier

#import pickle
#with open('donnees', 'wb') as fichier:
#    mon_pickler = pickle.Pickler(fichier)
# enregistrement ...

#---------------------------------------------------------------------

# 1 pickle / 1 objet

import pickle
score = {
    "joueur 1":    5,
    "joueur 2":   35,
    "joueur 3":   20,
    "joueur 4":    2,
}
with open('donnees', 'wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(score)

with open('donnees', 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    score_recupere = mon_depickler.load()
    print(score_recupere)

print("----")

#---------------------------------------------------------------------

# 1 pickle / 2 objets

import pickle

# INIT
score = {
    "joueur 1":    5,
    "joueur 2":   35,
    "joueur 3":   20,
    "joueur 4":    2,
}
score2 = {
    "joueur 10":  50,
    "joueur 20": 350,
    "joueur 30": 200,
    "joueur 40":  20,
}

# WRITE
with open('donnees2', 'wb') as fichier:     # w = write, b = binary
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(score)                 # save objet "score"
    mon_pickler.dump(score2)                # save objet "score2"

# READ
with open('donnees2', 'rb') as fichier:     # r = read, b = binary
    mon_depickler = pickle.Unpickler(fichier)
    score_recupere_A = mon_depickler.load() # call le 1er objet (score)
    score_recupere_B = mon_depickler.load() # call le 2nd objet (score2)
    print(score_recupere_A)
    print(score_recupere_B)

print("----")

#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------

input("Appuyez sur ENTREE pour fermer ce programme...")
