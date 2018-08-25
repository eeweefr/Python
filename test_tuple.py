#!/usr/bin/python
# -*-coding:Utf-8 -*

#---------------------------------------------------------------------

"""
Les tuples sont des listes immuables, qu'on ne peut modifier.
Un tuple se définit comme une liste, sauf qu'on utilise comme délimiteur des parenthèses au lieu des crochets.

À la différence des listes, les tuples, une fois créés, ne peuvent être modifiés :
on ne peut plus y ajouter d'objet ou en retirer.
"""

#---------------------------------------------------------------------

help(tuple)

#---------------------------------------------------------------------

tuple_vide = ()
tuple_non_vide = (1,) # est équivalent à ci dessous
tuple_non_vide = 1,
tuple_avec_plusieurs_valeurs = (1, 2, 5)

#---------------------------------------------------------------------

a, b = 3, 4
# égal à
(a, b) = (3, 4)

#---------------------------------------------------------------------

def decomposer(entier, divise_par):
    """Cette fonction retourne la partie entière
    et le reste de entier / divise_par"""

    p_e = entier // divise_par
    reste = entier % divise_par
    return p_e, reste

partie_entiere, reste = decomposer(20, 3)
print(partie_entiere)
print(reste)

aaa = decomposer(20, 3)
print( aaa )

#---------------------------------------------------------------------

input("Appuyez sur ENTREE pour fermer ce programme...")
