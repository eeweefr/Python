#!/usr/bin/python
# -*-coding:Utf-8 -*

#---------------------------------------------------------------------
# SOURCE : https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/232520-portee-des-variables-et-references
#
# Portees des variables
#   local
#   reference
#   global
#---------------------------------------------------------------------

"""
NOTE :
Attention, Les variables avant la fonction sont accessibles dans la fonction.
"""

a = 5
def print_a():
    """Fonction chargée d'afficher la variable a.
    Cette variable a n'est pas passée en paramètre de la fonction.
    On suppose qu'elle a été créée en dehors de la fonction, on veut voir
    si elle est accessible depuis le corps de la fonction"""

    print("La variable a = {0}.".format(a))

print_a()
#La variable a = 5.

a = 8
print_a()
#La variable a = 8.

print("----")

#---------------------------------------------------------------------

def set_var(nouvelle_valeur):
    """Fonction nous permettant de tester la portée des variables
    définies dans notre corps de fonction"""

    # On essaye d'afficher la variable var, si elle existe
    try:
        print("Avant l'affectation, notre variable var vaut {0}.".format(var))
    except NameError:
        print("La variable var n'existe pas encore.")
    var = nouvelle_valeur
    print("Après l'affectation, notre variable var vaut {0}.".format(var))

set_var(5)
#print(var) # Renvoie un erreur (normal) car var est local à la fonction.

print("----")

#---------------------------------------------------------------------

"""
Dans le corps de fonction, si vous faites "parametre = nouvelle_valeur", 
le paramètre ne sera modifié que dans le corps de la fonction. 
Alors que si vous faites "parametre.methode_pour_modifier(…)", l'objet derrière le paramètre sera bel et bien modifié.
"""

def ajouter(liste, valeur_a_ajouter):
    """Cette fonction insère à la fin de la liste la valeur que l'on veut ajouter"""
    liste.append(valeur_a_ajouter)

ma_liste=['a', 'e', 'i']
ajouter(ma_liste, 'o')
print(ma_liste)
#['a', 'e', 'i', 'o']

print("----")

#---------------------------------------------------------------------

# Reference

"""
LIST :
"ma_liste1" et "ma_liste2" contiennent une référence vers le même objet : 
si on modifie l'objet depuis une des deux variables, le changement sera visible depuis les deux variables.

INT, FLOAT, STRING :
Les entiers, les flottants, les chaînes de caractères, n'ont aucune méthode travaillant sur l'objet lui-même. 
Les chaînes de caractères, comme nous l'avons vu, ne modifient pas l'objet appelant mais renvoient un nouvel objet 
modifié. 
Et comme nous venons de le voir, le processus d'affectation n'est pas du tout identique à un appel de méthode.
"""

print("# LIST (reference) :")

ma_liste1 = [1, 2, 3]
ma_liste2 = ma_liste1
ma_liste2.append(4)
print(ma_liste2)
#[1, 2, 3, 4]
print(ma_liste1)
#[1, 2, 3, 4]

print("----")

#---------------------------------------------------------------------

# COPIER UNE "LIST"

print("# LIST (copy) :")

ma_liste1 = [1, 2, 3]
ma_liste2 = list(ma_liste1) # Cela revient à copier le contenu de ma_liste1
ma_liste2.append(4)

print(ma_liste2)
#[1, 2, 3, 4]
print(ma_liste1)
#[1, 2, 3]

print("----")

#---------------------------------------------------------------------

# DICT : idem que pour une LIST. Sera passé en référence.

print("# DICT (reference) :")

mon_dictionnaire1 = {"pseudo":"Prolixe", "mdp": "*", "pseudo":"6pril"}
mon_dictionnaire2 = mon_dictionnaire1
mon_dictionnaire2['toto'] = "titi"

print(mon_dictionnaire1)
print(mon_dictionnaire2)

print("----")

#---------------------------------------------------------------------

# COPIER UN "DICT"

print("# DICT (copy) :")

mon_dictionnaire1 = {"pseudo":"Prolixe", "mdp": "*", "pseudo":"6pril"}
mon_dictionnaire2 = dict(mon_dictionnaire1) # Cela revient à copier le contenu de mon_dictionnaire1
mon_dictionnaire2['toto'] = "titi"

print(mon_dictionnaire1)
print(mon_dictionnaire2)

print("----")

#---------------------------------------------------------------------

ma_liste1 = [1, 2]
ma_liste2 = [1, 2]

print("ma_liste1 et ma_liste2 ont le meme contenu : ",ma_liste1 == ma_liste2) # On compare le contenu des listes
#True
print("ma_liste1 et ma_liste2 n'ont pas la meme reference : ",ma_liste1 is ma_liste2) # On compare leur référence
#False

print("id() Renvoie la position de l'objet dans la mémoire Python sous la forme d'un entier :")
print("---->",id(ma_liste1))
print("---->",id(ma_liste2))
help(id)
#---------------------------------------------------------------------

i = 4 # Une variable, nommée i, contenant un entier
def inc_i():
    """Fonction chargée d'incrémenter i de 1"""
    global i # Python recherche i en dehors de l'espace local de la fonction
    i += 1

print(i)
#4
inc_i()
print(i)
#5

#---------------------------------------------------------------------

"""
CONCLUSION :

1/ Les variables locales définies avant l'appel d'une fonction seront accessibles, depuis le corps de la fonction, en lecture seule.

2/ Une variable locale définie dans une fonction sera supprimée après l'exécution de cette fonction.

3/ On peut cependant appeler les attributs et méthodes d'un objet pour le modifier durablement.

4/ Les variables globales se définissent à l'aide du mot-clé "global" suivi du nom de la variable préalablement créée.

5/ Les variables globales peuvent être modifiées depuis le corps d'une fonction (à utiliser avec prudence).
"""

#---------------------------------------------------------------------

input("Appuyez sur ENTREE pour fermer ce programme...")
