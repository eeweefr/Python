#!/usr/bin/python
# -*-coding:Utf-8 -*

from package.fonctions import table, toto
table(5) # Appel de la fonction table
print("toto : ", toto())

# Ou ...
"""
import package.fonctions
package.fonctions.table(5)  # Appel de la fonction table
print( package.fonctions.toto() )
"""

input("Appuyez sur ENTREE pour fermer ce programme...")
