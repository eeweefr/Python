#!/usr/bin/python
# -*-coding:Utf-8 -*

numerateur = 3
denominateur = 4

try:
    resultat = numerateur / denominateur
except NameError:
    print("La variable numerateur ou denominateur n'a pas été définie.")
except TypeError:
    print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
except ZeroDivisionError:
    print("La variable denominateur est égale à 0.")
except type_de_l_exception as exception_retournee:
    print("Voici l'erreur :", exception_retournee)
except type_de_l_exception:  # Rien ne doit se passer en cas d'erreur (utiliser : pass)
    pass
else:
    print("Le résultat obtenu est", resultat)
finally:
    # Instruction(s) exécutée(s) qu'il y ait eu des erreurs ou non
    print("finally iciiiiiii")

input("Appuyez sur ENTREE pour fermer ce programme...")
