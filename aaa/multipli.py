"""module multipli contenant la fonction table"""

def table(nb, max=10):
    """Fonction affichant la table de multiplication par nb de
    1 * nb jusqu'à max * nb"""
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1

# Uniquement à __main__ s'il s'agit du fichier executé. S'il est call par un autre fichier, il aura pour valeur multipli
if "__main__" == __name__:
    table(4)
