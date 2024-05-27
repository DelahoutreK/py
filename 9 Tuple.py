<<<<<<< HEAD
# Surprise, c'est très court car quasiment identique aux listes!

# se déclare de la même facon a deux exception! un tupel utilise des () et un tupel contenant un seul objet nécéssite une virgule
tuple1 = (1,2) # pour un tuple d'une valeur on aurait noté tuple1 = (1,)
print(tuple1)

# similairement un tupel indexe de 0 à x, peut contenir plusieurs fois la meme valeur, les types a l'interieur importent peu
# et les memes fonctions et methodes peuvent etre utilisées (tant qu'elles ne modifient pas le tupel), quelques unes listées ici.
"""
len()
print(tupelname[index])
if value in tupel:
loop
concatene two tupel en un nouveau (t3= t1+t2) car on en crée un 3 sans modifier les précédents

"""
# en revanche un tupel est innaltérable cad, pas de modification à l'interieur de celui ci. A l'exception d'une méthode détournée
# Convertir le tupel en liste puis en tupel a nouveau
tuple2 = list(tuple1)
tuple2[1] = "vache"
tuple1 = tuple(tuple2)
print(tuple1)

# possibilité d'assigner des values a des variables (unpacking, contrairement a définir le tuple qui est packing)
(nombre,animal) = tuple1

print(nombre)
print(animal)

# en utilisant une * on peut attribuer toutes les valeurs restantes a une variable
alphbt = ("a","l","p","h","b","t")

(lettre1,lettre2,*rest) = alphbt
print(rest) # lettre1 aura "a" et lettre2 aura "l"
=======
# Surprise, c'est très court car quasiment identique aux listes!

# se déclare de la même facon a deux exception! un tupel utilise des () et un tupel contenant un seul objet nécéssite une virgule
tuple1 = (1,2) # pour un tuple d'une valeur on aurait noté tuple1 = (1,)
print(tuple1)

# similairement un tupel indexe de 0 à x, peut contenir plusieurs fois la meme valeur, les types a l'interieur importent peu
# et les memes fonctions et methodes peuvent etre utilisées (tant qu'elles ne modifient pas le tupel), quelques unes listées ici.
"""
len()
print(tupelname[index])
if value in tupel:
loop
concatene two tupel en un nouveau (t3= t1+t2) car on en crée un 3 sans modifier les précédents

"""
# en revanche un tupel est innaltérable cad, pas de modification à l'interieur de celui ci. A l'exception d'une méthode détournée
# Convertir le tupel en liste puis en tupel a nouveau
tuple2 = list(tuple1)
tuple2[1] = "vache"
tuple1 = tuple(tuple2)
print(tuple1)

# possibilité d'assigner des values a des variables (unpacking, contrairement a définir le tuple qui est packing)
(nombre,animal) = tuple1

print(nombre)
print(animal)

# en utilisant une * on peut attribuer toutes les valeurs restantes a une variable
alphbt = ("a","l","p","h","b","t")

(lettre1,lettre2,*rest) = alphbt
print(rest) # lettre1 aura "a" et lettre2 aura "l"
>>>>>>> 221797b3f7397187369c1a66c82e768c350a3a1e
# note, attribuer * a lettre2 aurait causé: lettre1 = a, lettre2 = lphb, rest=t