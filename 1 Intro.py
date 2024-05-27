<<<<<<< HEAD
# les quotes "" et '' sont toutes les deux valides pour déclarer une string
# python est "case sensitive" c'est a dire: a != A

# dans python l'indentation est importante
# elle indique un bloc de code

# Example
# if 5 > 2:
#    print("5 plus grand que 2")

# Example (erreur)
# if 5>2:
# print("( plus grand que 2")

# un bloc de code contiendra toujours le meme nombre d'espace 
# x=input('inserez valeur de x')
# y=input('inserez valeur de y')

""""py
if x > y:
    print('X('+x+')est plus grand que Y('+y+')')
    print(":)") # notez, l'espace avant les prints est equivalent pour les lignes 17 et 18 
elif y > x:
    print('Y('+y+')est plus grand que X('+x+')')
else:
    print("X("+x+") et Y("+y+") sont égaux")
"""

# pas de mot clé pour les variables / no keyword to declare 
# x = value

# les commentaires sont faits via "#" 
# il n'y a pas de commentaire multiligne sur python 
# il est tout de meme possible d'utiliser des strings multilignes car python les ignore si elles ne sont pas attribuées a une variable
""""py
comme ca en theorie / like that 
"""

# il est possible de cast une variable sur python
""""py
a = str (3)  # 3 est une str, une string
b = int(3)   # 3 est un int, une integer
c = float(3) # 3 est un float
"""

# il existe une fonction permettant de montrer le type d'une variable
# type
# print(type(a)) affichera "class str"


# déclaration de variables
# une variable ne peut pas
#   commencer par un chiffre, contenir des "-" ou espaces, etre un mot clé python

# il est possible d'attribuer plusieurs valeurs a plusieurs variables et inversement tel que
""""py
e,f,g = str(1),str(2),str(3)
print (e+" "+f+" "+g)
h = i = j = "bleu"
print (h+i+j)
"""

# dans la meme idée une variable contenant plus d'une valeur, un tableau (collection dans python), peut etre "unpacked"
""""py
colors = ["bleu","rouge","violet"]
k,l,m = colors
print (k+l+m)
"""

# la concatenation se fera via l'operateur + comme deja observé dans ce tuto. Notez qu'il n'inclus pas d'espace
# ainsi le point précédent print(k+l+m) affichera bleurougeviolet
# dans le cas de deux int ou deux float pas de probleme
# il est en revanche impossible de str + int ou int + float
# une solution etant d'utiliser des , pour les afficher ensemble 

# example
""""py
o = 2
p = "voitures"
print(o,p)
"""
=======
# les quotes "" et '' sont toutes les deux valides pour déclarer une string
# python est "case sensitive" c'est a dire: a != A

# dans python l'indentation est importante
# elle indique un bloc de code

# Example
# if 5 > 2:
#    print("5 plus grand que 2")

# Example (erreur)
# if 5>2:
# print("( plus grand que 2")

# un bloc de code contiendra toujours le meme nombre d'espace 
# x=input('inserez valeur de x')
# y=input('inserez valeur de y')

""""py
if x > y:
    print('X('+x+')est plus grand que Y('+y+')')
    print(":)") # notez, l'espace avant les prints est equivalent pour les lignes 17 et 18 
elif y > x:
    print('Y('+y+')est plus grand que X('+x+')')
else:
    print("X("+x+") et Y("+y+") sont égaux")
"""

# pas de mot clé pour les variables / no keyword to declare 
# x = value

# les commentaires sont faits via "#" 
# il n'y a pas de commentaire multiligne sur python 
# il est tout de meme possible d'utiliser des strings multilignes car python les ignore si elles ne sont pas attribuées a une variable
""""py
comme ca en theorie / like that 
"""

# il est possible de cast une variable sur python
""""py
a = str (3)  # 3 est une str, une string
b = int(3)   # 3 est un int, une integer
c = float(3) # 3 est un float
"""

# il existe une fonction permettant de montrer le type d'une variable
# type
# print(type(a)) affichera "class str"


# déclaration de variables
# une variable ne peut pas
#   commencer par un chiffre, contenir des "-" ou espaces, etre un mot clé python

# il est possible d'attribuer plusieurs valeurs a plusieurs variables et inversement tel que
""""py
e,f,g = str(1),str(2),str(3)
print (e+" "+f+" "+g)
h = i = j = "bleu"
print (h+i+j)
"""

# dans la meme idée une variable contenant plus d'une valeur, un tableau (collection dans python), peut etre "unpacked"
""""py
colors = ["bleu","rouge","violet"]
k,l,m = colors
print (k+l+m)
"""

# la concatenation se fera via l'operateur + comme deja observé dans ce tuto. Notez qu'il n'inclus pas d'espace
# ainsi le point précédent print(k+l+m) affichera bleurougeviolet
# dans le cas de deux int ou deux float pas de probleme
# il est en revanche impossible de str + int ou int + float
# une solution etant d'utiliser des , pour les afficher ensemble 

# example
""""py
o = 2
p = "voitures"
print(o,p)
"""
>>>>>>> 221797b3f7397187369c1a66c82e768c350a3a1e
