<<<<<<< HEAD
# rappel, les strings sont déclarées avec des '' ou ""

print("bonjour") # declaration string
print("bonjour je m'appelle 'John'") # string incluant '
print('son nom est "John"') # string incluant ""

# rappel, les strings multilignes peuvent etre utilisées comme commentaires ou etres attribuées, ceci fonctionne avec """ """ et ''' '''
a = """une 
bonne string
multiligne
"""
print(a)

# il est possible d'identifier un charactere dans une string, la premiere lettre est 0
print(a[0]) 

# les strings etant des arrays, il est possible d'utiliser des boucles pour chaque charactere 
for x in a:
    print(x)

# String length (longueur), via la fonction len()
print(len(a))

# check string, via la fonction in (verifier qu'une variable contient notre string). Utilisable avec des if!
print("bonne" in a) # True
print("aziheaih" in a) # False
# note, utiliser "not in" vérifier si la string n'est PAS dans notre variable

# slicing (séparer les strings)

# slice des charactères spécifiques
print(a[1:3:5])
# slice du debut jusqu'au charactère X
print(a[:12])
# slice en partant de la fin
print(a[-15:-10])

# modifications de string
"""
var.upper(): mets tout en majuscule
var.lower(): mets tout en minuscule
var.strip(): retire les espaces
var.replace(texte,texte): remplace des charactères par d'autres
var.split("charactere"): sépare la string en substring si "charactere" est détecté
"""

# concatenation utilise toujours +

# concatener str et int/float 
# ajouter un f et un placeholder {variable}
b = 12
c = f"j'ai {b} bananes"
print(c)

# un placeholder peut inclure des modifications ou restrictions ou du code/fonctions
c = f"j'ai {b:.2f} bananes" # modifie b pour qu'il soit un nombre a virgule avec 2 chiffres apres la virgule
print(c)

# pour ignorer un charactere on utilisera un antislash/backslash tel que
print("\"")

# il existe une tonne de methods que je ne vais pas lister ici, google est votre ami
# quelques exemples utiles tout de meme
"""
capitalize()
count()
lower()
upper()
partition()
split()
strip()
"""

=======
# rappel, les strings sont déclarées avec des '' ou ""

print("bonjour") # declaration string
print("bonjour je m'appelle 'John'") # string incluant '
print('son nom est "John"') # string incluant ""

# rappel, les strings multilignes peuvent etre utilisées comme commentaires ou etres attribuées, ceci fonctionne avec """ """ et ''' '''
a = """une 
bonne string
multiligne
"""
print(a)

# il est possible d'identifier un charactere dans une string, la premiere lettre est 0
print(a[0]) 

# les strings etant des arrays, il est possible d'utiliser des boucles pour chaque charactere 
for x in a:
    print(x)

# String length (longueur), via la fonction len()
print(len(a))

# check string, via la fonction in (verifier qu'une variable contient notre string). Utilisable avec des if!
print("bonne" in a) # True
print("aziheaih" in a) # False
# note, utiliser "not in" vérifier si la string n'est PAS dans notre variable

# slicing (séparer les strings)

# slice des charactères spécifiques
print(a[1:3:5])
# slice du debut jusqu'au charactère X
print(a[:12])
# slice en partant de la fin
print(a[-15:-10])

# modifications de string
"""
var.upper(): mets tout en majuscule
var.lower(): mets tout en minuscule
var.strip(): retire les espaces
var.replace(texte,texte): remplace des charactères par d'autres
var.split("charactere"): sépare la string en substring si "charactere" est détecté
"""

# concatenation utilise toujours +

# concatener str et int/float 
# ajouter un f et un placeholder {variable}
b = 12
c = f"j'ai {b} bananes"
print(c)

# un placeholder peut inclure des modifications ou restrictions ou du code/fonctions
c = f"j'ai {b:.2f} bananes" # modifie b pour qu'il soit un nombre a virgule avec 2 chiffres apres la virgule
print(c)

# pour ignorer un charactere on utilisera un antislash/backslash tel que
print("\"")

# il existe une tonne de methods que je ne vais pas lister ici, google est votre ami
# quelques exemples utiles tout de meme
"""
capitalize()
count()
lower()
upper()
partition()
split()
strip()
"""

>>>>>>> 221797b3f7397187369c1a66c82e768c350a3a1e
