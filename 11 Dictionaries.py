<<<<<<< HEAD
# key - value, collections. Ordonnés, changeables mais sans duplications de clé-valeur. type des valeurs non important
dict1 = {
    "name":"Morello",
    "fname":"John",
    "gender":"Male",
    "dob":"07/05/99"
}

# acceder aux valeurs
print(dict1["name"])
# via method
x = dict1.get("dob")
print(x)

# voir clés/valeurs
dict1.keys() # dict1.values()

# obtenir objets, renvoie les paires
x = dict1.items()
print(x)
# bien sur, in ou une boucle permet de verifier l'existence des objets dans un dictionnaire.

# update dictionnary
dict1.update({"gender":"female"})
print(x)

# ajout
dict1["city"] = "Tintigny"
print(x)

# suppression
dict1.pop("fname") # del() fonctionne aussi mais peut aussi supprimer tout le dict
print(x)

# vider les entrées 
dict1.clear()
print(x)

# copier
dict2 = dict1.copy()
print(dict2)        # rappel, dict1 est vide!

# un dict peut en contenir d'autres, on parlera de "nested dict"
tcho = {
    "tcho1" :{
        "fname": "Jean",
        "gender": "m"
    },
    "tcho2" :{
        "fname": "Camille",
        "gender": "m"
    }
}
# les acces se feront ainsi
print(tcho["tcho2"]["fname"])


# prend des methodes similaires au sets etc...
"""
len()
loop! et oui, encore
=======
# key - value, collections. Ordonnés, changeables mais sans duplications de clé-valeur. type des valeurs non important
dict1 = {
    "name":"Morello",
    "fname":"John",
    "gender":"Male",
    "dob":"07/05/99"
}

# acceder aux valeurs
print(dict1["name"])
# via method
x = dict1.get("dob")
print(x)

# voir clés/valeurs
dict1.keys() # dict1.values()

# obtenir objets, renvoie les paires
x = dict1.items()
print(x)
# bien sur, in ou une boucle permet de verifier l'existence des objets dans un dictionnaire.

# update dictionnary
dict1.update({"gender":"female"})
print(x)

# ajout
dict1["city"] = "Tintigny"
print(x)

# suppression
dict1.pop("fname") # del() fonctionne aussi mais peut aussi supprimer tout le dict
print(x)

# vider les entrées 
dict1.clear()
print(x)

# copier
dict2 = dict1.copy()
print(dict2)        # rappel, dict1 est vide!

# un dict peut en contenir d'autres, on parlera de "nested dict"
tcho = {
    "tcho1" :{
        "fname": "Jean",
        "gender": "m"
    },
    "tcho2" :{
        "fname": "Camille",
        "gender": "m"
    }
}
# les acces se feront ainsi
print(tcho["tcho2"]["fname"])


# prend des methodes similaires au sets etc...
"""
len()
loop! et oui, encore
>>>>>>> 221797b3f7397187369c1a66c82e768c350a3a1e
"""