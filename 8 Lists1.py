<<<<<<< HEAD
# basiquement ce sont des tableaux, des arrays (python les appelle Collections) et elles peuvent etre forcecast avec list(("value"))
liste1 = ["a","b","c","d"]
print(liste1)
# a est index 0
# ajouter a la liste ajoutera a l'index suivant cad [4], apres d
# il peut y avoir des duplicatas dans une liste 
liste1.append("a")
print(liste1)

# les types dans une liste ne sont pas importants
liste1.append(5)
liste1.append(True)
liste1.append("p")
print(liste1)

# comme montré précédement on peut acceder aux valeurs a indexes (oui, une string est techniquement une array de charactères)
# l'acces au valeurs d'une liste est identique a celles d'une array print(liste[index])
# il est de la meme facon possible de verifier la présence de valeurs if 5 in liste1 print("yep")

# modifications de listes
liste1[2] = 3   # oui, comme si on re-attribue une variable
print(liste1)
# de meme, on peut modifier une range liste1[1:3]=[value,value,value]
# modifier une range et mettre plus de valeurs que la taille de la range les ajoutera a la suite des modifications. Moins de valeurs aura un effet similaire mais en suppression
listeRange = [1,2,3,4,5]
listeRange[1:2] = ["a","b","c"] # 2 et 3 remplacés par a et b respectivement, c ajouté a leur droite
print(listeRange)

listeRange[1:3] = ["poulet"] # b sera supprimé
print(listeRange)

# insertion list.insert(index,value)
liste2 = ["a","b","c"]
liste2.insert(1,"insertion")
print(liste2)

# pour insérer a la fin/ajouter a la liste 
liste2.append("ajout")
print(liste2)

# pour ajouter une liste a une autre
liste1.extend(liste2)
print(liste1) 
# Note, n'importe quel objet iterable peut etre extend dans une liste, incluant les tuple, sets, etc...)

# suppressions
# via remove()
liste1.remove("a") # supprimera uniquement la premiere valeur de type string contenant a.
print(liste1)

# via pop(), sans indexe donnée pop retirera le dernier indexe
liste1.pop(3) # retirera l'objet d'indexe 3, un "a" dans notre cas
print(liste1) # ce resultat peut etre obtenu via del liste1[3], en revanche del liste1 a la capacité de supprimer toute la liste.

# vider la liste
liste1.clear()
print(liste1)
del liste1 # ca sera utile pour le prochain concept

# il est généralement utile de créer des boucles pour voir le contenu d'une liste, je ne détaillerai pas cette methode ici

# une application utile de python est "la compréhension de liste" permettant de coder de nouvelles listes basées sur une autre liste existante
# syntaxe: nomliste = [expression for objet in iterable if condition == True] (la condition est optionelle)
liste1 = [x for x in liste2 if "a" in x] # cette boucle va sélectionner toutes les valeurs contenant "a" et créer une liste1 les incluant
print(liste1)


# les listes ont des fonctions applicables
"""
len()   longueur de la liste 
=======
# basiquement ce sont des tableaux, des arrays (python les appelle Collections) et elles peuvent etre forcecast avec list(("value"))
liste1 = ["a","b","c","d"]
print(liste1)
# a est index 0
# ajouter a la liste ajoutera a l'index suivant cad [4], apres d
# il peut y avoir des duplicatas dans une liste 
liste1.append("a")
print(liste1)

# les types dans une liste ne sont pas importants
liste1.append(5)
liste1.append(True)
liste1.append("p")
print(liste1)

# comme montré précédement on peut acceder aux valeurs a indexes (oui, une string est techniquement une array de charactères)
# l'acces au valeurs d'une liste est identique a celles d'une array print(liste[index])
# il est de la meme facon possible de verifier la présence de valeurs if 5 in liste1 print("yep")

# modifications de listes
liste1[2] = 3   # oui, comme si on re-attribue une variable
print(liste1)
# de meme, on peut modifier une range liste1[1:3]=[value,value,value]
# modifier une range et mettre plus de valeurs que la taille de la range les ajoutera a la suite des modifications. Moins de valeurs aura un effet similaire mais en suppression
listeRange = [1,2,3,4,5]
listeRange[1:2] = ["a","b","c"] # 2 et 3 remplacés par a et b respectivement, c ajouté a leur droite
print(listeRange)

listeRange[1:3] = ["poulet"] # b sera supprimé
print(listeRange)

# insertion list.insert(index,value)
liste2 = ["a","b","c"]
liste2.insert(1,"insertion")
print(liste2)

# pour insérer a la fin/ajouter a la liste 
liste2.append("ajout")
print(liste2)

# pour ajouter une liste a une autre
liste1.extend(liste2)
print(liste1) 
# Note, n'importe quel objet iterable peut etre extend dans une liste, incluant les tuple, sets, etc...)

# suppressions
# via remove()
liste1.remove("a") # supprimera uniquement la premiere valeur de type string contenant a.
print(liste1)

# via pop(), sans indexe donnée pop retirera le dernier indexe
liste1.pop(3) # retirera l'objet d'indexe 3, un "a" dans notre cas
print(liste1) # ce resultat peut etre obtenu via del liste1[3], en revanche del liste1 a la capacité de supprimer toute la liste.

# vider la liste
liste1.clear()
print(liste1)
del liste1 # ca sera utile pour le prochain concept

# il est généralement utile de créer des boucles pour voir le contenu d'une liste, je ne détaillerai pas cette methode ici

# une application utile de python est "la compréhension de liste" permettant de coder de nouvelles listes basées sur une autre liste existante
# syntaxe: nomliste = [expression for objet in iterable if condition == True] (la condition est optionelle)
liste1 = [x for x in liste2 if "a" in x] # cette boucle va sélectionner toutes les valeurs contenant "a" et créer une liste1 les incluant
print(liste1)


# les listes ont des fonctions applicables
"""
len()   longueur de la liste 
>>>>>>> 221797b3f7397187369c1a66c82e768c350a3a1e
"""