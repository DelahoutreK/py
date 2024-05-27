<<<<<<< HEAD
# un set est un ensemble, une collection. Il est non indexé et les objets n'y ont pas d'ordre et le type des valeurs n'est pas important. 
# Un set n'autorise pas de duplicatas de valeurs et ses valeurs ne sont pas modifiables. En revanche, on peut y ajouter et retirer des valeurs.
# Note, 1 et True sont la meme valeur tout comme 0 et False

trucsEcrits = {"lettre","livre","texte"}
print(trucsEcrits) # en lancant ce fichier dans le terminal on peut voir le "manque d'ordre"

# un set utilise des methodes similaires aux tuples et listes
"""
len()
if value in tupel:
loop
"""

# pour acceder aux valeurs d'un set utiliser un index est impossible. Rappel d'une boucle
for x in trucsEcrits:
    print(x)

# ajouter un elementa un set
trucsEcrits.add("notes")
print(trucsEcrits)

# ajouter un itterable a un set
set2 = {"diplome","recommandé","certificat"}
trucsEcrits.update(set2)
print(trucsEcrits)

# retirer un objet
trucsEcrits.remove("diplome")
print(trucsEcrits)

# retirer un truc sans avoir d'erreur quand l'objet n'existe pas
trucsEcrits.discard("spitfire")

# note pop() fonctionne mais retire un objet au hasard
# clear() rendra le set vide
# del() supprimera le set

# jointures de sets

# union, deux (ou plus) sets font un troisieme set. Fonctionne avec Tuple via union SEULEMENT
tartesAuxFruits = {"aux pommes","a la cerise","a l'orange"}
autresTartes = {"aux thon","dans ta gueule"}

tartes = tartesAuxFruits.union(autresTartes)    # notes plusieurs sets peuvente etre joints (set2,set3,...) 
print(tartes)                                   # | est identique a union, on notera setN = set1 | set2 | set3 ... (ceci ne fonctionne pas pour tupel x set)
# les duplicatas de réponses seront supprimés pour n'en garder qu'un

# intersection(), similairement mais garde uniquement les objets de meme valeur pour créer un nouveau set
setEx1 = {1,2,3,4}
setEx2 = {1,3,5,7}

setEx3 = setEx1.intersection(setEx2)    # & désigne aussi une intersection
print(setEx3)                           # & ne fonctionne que pour set x set

# note, intersection_update() a le meme effet mais modifie le premier set et le retourne au lieu d'en créer un
# de ce fait set1.intersection_update(set2) supprimera tous les objets n'etant pas dans 1 ET 2 et retournera uniquement les objets communs dans 1.

# difference(). Garde les objets non communs aux sets comparés dans un nouveau set.
# - est un opérateur fonctionel pour cette manipulation mais ne permet que le set x set
# difference_update() aura un effet comme intersection_update() mais pour difference
# symmetric_difference() aura un effet similaire mais gardera les elements non communs de  tous les sets analysés dans un nouveau set
# ^ pour symmetric_difference() de set x set
# symmetric_difference_update() c'est sym_dif mais retourné sur le set 1

# plein de methodes a regarder en ligne
=======
# un set est un ensemble, une collection. Il est non indexé et les objets n'y ont pas d'ordre et le type des valeurs n'est pas important. 
# Un set n'autorise pas de duplicatas de valeurs et ses valeurs ne sont pas modifiables. En revanche, on peut y ajouter et retirer des valeurs.
# Note, 1 et True sont la meme valeur tout comme 0 et False

trucsEcrits = {"lettre","livre","texte"}
print(trucsEcrits) # en lancant ce fichier dans le terminal on peut voir le "manque d'ordre"

# un set utilise des methodes similaires aux tuples et listes
"""
len()
if value in tupel:
loop
"""

# pour acceder aux valeurs d'un set utiliser un index est impossible. Rappel d'une boucle
for x in trucsEcrits:
    print(x)

# ajouter un elementa un set
trucsEcrits.add("notes")
print(trucsEcrits)

# ajouter un itterable a un set
set2 = {"diplome","recommandé","certificat"}
trucsEcrits.update(set2)
print(trucsEcrits)

# retirer un objet
trucsEcrits.remove("diplome")
print(trucsEcrits)

# retirer un truc sans avoir d'erreur quand l'objet n'existe pas
trucsEcrits.discard("spitfire")

# note pop() fonctionne mais retire un objet au hasard
# clear() rendra le set vide
# del() supprimera le set

# jointures de sets

# union, deux (ou plus) sets font un troisieme set. Fonctionne avec Tuple via union SEULEMENT
tartesAuxFruits = {"aux pommes","a la cerise","a l'orange"}
autresTartes = {"aux thon","dans ta gueule"}

tartes = tartesAuxFruits.union(autresTartes)    # notes plusieurs sets peuvente etre joints (set2,set3,...) 
print(tartes)                                   # | est identique a union, on notera setN = set1 | set2 | set3 ... (ceci ne fonctionne pas pour tupel x set)
# les duplicatas de réponses seront supprimés pour n'en garder qu'un

# intersection(), similairement mais garde uniquement les objets de meme valeur pour créer un nouveau set
setEx1 = {1,2,3,4}
setEx2 = {1,3,5,7}

setEx3 = setEx1.intersection(setEx2)    # & désigne aussi une intersection
print(setEx3)                           # & ne fonctionne que pour set x set

# note, intersection_update() a le meme effet mais modifie le premier set et le retourne au lieu d'en créer un
# de ce fait set1.intersection_update(set2) supprimera tous les objets n'etant pas dans 1 ET 2 et retournera uniquement les objets communs dans 1.

# difference(). Garde les objets non communs aux sets comparés dans un nouveau set.
# - est un opérateur fonctionel pour cette manipulation mais ne permet que le set x set
# difference_update() aura un effet comme intersection_update() mais pour difference
# symmetric_difference() aura un effet similaire mais gardera les elements non communs de  tous les sets analysés dans un nouveau set
# ^ pour symmetric_difference() de set x set
# symmetric_difference_update() c'est sym_dif mais retourné sur le set 1

# plein de methodes a regarder en ligne
>>>>>>> 221797b3f7397187369c1a66c82e768c350a3a1e
