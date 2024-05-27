<<<<<<< HEAD
# ce fichier a pour seul but d'ajouter des détails de l'intro quant a la déclaration et utilisation de variables

# variables globales
# une variable  crée en dehors d'une fonction sera qualifiée de variable globale et accessible n'importe où
""""py
a = 12

def maFct():
    print(a)
maFct()
"""
# utiliser une variable portant le meme nom dans une fonction la rédéfini localement, cad dans maFct2() b vaut 1, en dehors b vaut 3
# dans la meme idée, déclarer une variable dans une fonction la rend locale et propre a cette fonction
""""py
b = 3
def maFct2():
    b = 1
    print(b)
maFct2()
print (b)
"""

# utiliser le mot clé global permet a une variable locale d'etre globale
""""py
def maFct3():
    global c
    c = 6 
maFct3()
print(c)
"""

# utiliser le mot clé global dans une fonction peut écraser la valeur d'une variable en dehors de cette fonction
""""py
d = 9
def maFct4():
    global d
    d = 5
maFct4()
print(d)
"""
=======
# ce fichier a pour seul but d'ajouter des détails de l'intro quant a la déclaration et utilisation de variables

# variables globales
# une variable  crée en dehors d'une fonction sera qualifiée de variable globale et accessible n'importe où
""""py
a = 12

def maFct():
    print(a)
maFct()
"""
# utiliser une variable portant le meme nom dans une fonction la rédéfini localement, cad dans maFct2() b vaut 1, en dehors b vaut 3
# dans la meme idée, déclarer une variable dans une fonction la rend locale et propre a cette fonction
""""py
b = 3
def maFct2():
    b = 1
    print(b)
maFct2()
print (b)
"""

# utiliser le mot clé global permet a une variable locale d'etre globale
""""py
def maFct3():
    global c
    c = 6 
maFct3()
print(c)
"""

# utiliser le mot clé global dans une fonction peut écraser la valeur d'une variable en dehors de cette fonction
""""py
d = 9
def maFct4():
    global d
    d = 5
maFct4()
print(d)
"""
>>>>>>> 221797b3f7397187369c1a66c82e768c350a3a1e
