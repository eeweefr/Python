#!/usr/bin/python
# -*-coding:Utf-8 -*

#---------------------------------------------------------------------

help(list)

#---------------------------------------------------------------------

ma_liste = list() # On crée une liste vide
print(type(ma_liste))
#<class 'list'>
print(ma_liste)
#[]

#---------------------------------------------------------------------

ma_liste = []
print(ma_liste)

#---------------------------------------------------------------------

ma_liste = [1, 2, 3, 4, 5] # Une liste avec cinq objets
print(ma_liste)
#[1, 2, 3, 4, 5]

#---------------------------------------------------------------------

ma_liste = [1, 3.5, "une chaine", []]

#---------------------------------------------------------------------

ma_liste = ['c', 'f', 'm']

print(ma_liste[0]) # On accède au premier élément de la liste
#'c'

print(ma_liste[2]) # Troisième élément
#'m'

ma_liste[1] = 'Z' # On remplace 'f' par 'Z'
print(ma_liste)
#['c', 'Z', 'm']

#---------------------------------------------------------------------

# APPEND : add en fin de tableau

ma_liste = [1, 2, 3]
ma_liste.append(56) # On ajoute 56 à la fin de la liste
print(ma_liste)
#[1, 2, 3, 56]

#---------------------------------------------------------------------

chaine1 = "une petite phrase"
chaine2 = chaine1.upper() # On met en majuscules chaine1
print(chaine1)                   # On affiche la chaîne d'origine
#'une petite phrase'
# Elle n'a pas été modifiée par la méthode upper

print(chaine2)                   # On affiche chaine2
'UNE PETITE PHRASE'
# C'est chaine2 qui contient la chaîne en majuscules
# Voyons pour les listes à présent

liste1 = [1, 5.5, 18]
liste2 = liste1.append(-15) # On ajoute -15 à liste1
print(liste1)                      # On affiche liste1
#[1, 5.5, 18, -15]
# Cette fois, l'appel de la méthode a modifié l'objet d'origine (liste1)
# Voyons ce que contient liste2

print(liste2)
# Rien ?
#None

#---------------------------------------------------------------------

# INSERT : add à l'index x

ma_liste = ['a', 'b', 'd', 'e']
ma_liste.insert(2, 'c') # On insère 'c' à l'indice 2
print(ma_liste)
#['a', 'b', 'c', 'd', 'e']

#---------------------------------------------------------------------

array1 = ["toto", "titi"]
array2 = array1.append("tete")
print( array2 )

array2 = array1
print( array2 )

#---------------------------------------------------------------------

# concaténer 2 tableaux

ma_liste1 = [3, 4, 5]
ma_liste2 = [8, 9, 10]
ma_liste1.extend(ma_liste2) # On insère ma_liste2 à la fin de ma_liste1
print(ma_liste1)
#[3, 4, 5, 8, 9, 10]

ma_liste1 = [3, 4, 5]
print(ma_liste1 + ma_liste2)
#[3, 4, 5, 8, 9, 10]

ma_liste1 += ma_liste2 # Identique à extend
print(ma_liste1)
#[3, 4, 5, 8, 9, 10]

#---------------------------------------------------------------------

# DEL : supp variable

variable = 34
print(variable)
#34

del variable
#print(variable)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'variable' is not defined


ma_liste = [-5, -2, 1, 4, 7, 10]
del ma_liste[0] # On supprime le premier élément de la liste
print(ma_liste)
#[-2, 1, 4, 7, 10]

del ma_liste[2] # On supprime le troisième élément de la liste
print(ma_liste)
#[-2, 1, 7, 10]

#---------------------------------------------------------------------

# REMOVE : supp 1er valeur d'une "list" correspondante

list = [1, "aaa", ["bbb"], "aaa", 55]
list.remove("aaa")
print(list)

#---------------------------------------------------------------------

# POP : supp index et le retourne

list = [45, "foo", "bar", "toto", 345]
print("valeur supp : ",list.pop(2))
print("result : ",list)

#---------------------------------------------------------------------

ma_liste = ['a', 'b', 'c']

# WHILE :
i = 0 # Notre indice pour la boucle while
while i < len(ma_liste):
    print(ma_liste[i])
    i += 1 # On incrémente i, ne pas oublier !




# FOR :
# Cette méthode est cependant préférable
for elt in ma_liste: # elt va prendre les valeurs successives des éléments de ma_liste
    print(elt)

#---------------------------------------------------------------------

ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i, elt in enumerate(ma_liste):
    print("À l'indice {} se trouve {}.".format(i, elt))

for elt in enumerate(ma_liste):
    print(elt)

#---------------------------------------------------------------------

autre_liste = [
    [1, 'a'],
    [4, 'd'],
    [7, 'g'],
    [26, 'z'],
]
for nb, lettre in autre_liste:
    print("La lettre {} est la {}e de l'alphabet.".format(lettre, nb))

#---------------------------------------------------------------------

input("Appuyez sur ENTREE pour fermer ce programme...")
