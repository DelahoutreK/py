<<<<<<< HEAD
# Arrangement de listes, numérique ET alphabétique
liste1 = [12,50,42,7,69]
liste1.sort()
print(liste1)

# pour changer le type d'arrangement
"""
sort(reverse = True)                        décroissant
sort(key = str.lower)                       case-insensitive
reverse()                                   inverse l'ordre actuel
"""
# via une fonction, il faut remplacer la clé par une fonction. Voici un exemple
def fct(n):
    return abs(n-10)    # abs, valeur absolue
liste1.sort(key = fct)  # ordonne liste1 tel que les chiffres le plus proche de 10 sont affichés en premier
print(liste1) 

# copier une liste
liste2 = liste1.copy() # meme effet que liste2 = list(liste1)
print(liste2)

# Joindre des listes
# pas d'exemples ici, on a vu ces methodes plus tot. Je vais tout de meme les lister 
"""
via la concaténation
via une boucle
via la method extend()
=======
# Arrangement de listes, numérique ET alphabétique
liste1 = [12,50,42,7,69]
liste1.sort()
print(liste1)

# pour changer le type d'arrangement
"""
sort(reverse = True)                        décroissant
sort(key = str.lower)                       case-insensitive
reverse()                                   inverse l'ordre actuel
"""
# via une fonction, il faut remplacer la clé par une fonction. Voici un exemple
def fct(n):
    return abs(n-10)    # abs, valeur absolue
liste1.sort(key = fct)  # ordonne liste1 tel que les chiffres le plus proche de 10 sont affichés en premier
print(liste1) 

# copier une liste
liste2 = liste1.copy() # meme effet que liste2 = list(liste1)
print(liste2)

# Joindre des listes
# pas d'exemples ici, on a vu ces methodes plus tot. Je vais tout de meme les lister 
"""
via la concaténation
via une boucle
via la method extend()
>>>>>>> 221797b3f7397187369c1a66c82e768c350a3a1e
"""