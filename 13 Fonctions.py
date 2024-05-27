# une fonction est un bloc de code utilisé sur commande
def fonctionCool(): # appel de définition
    print("Je suis une fonction") # code utilisé en lancant la fonction
fonctionCool() # appel/utilisation de la fonction

# une fonction peut utiliser des arguments/parametres
def noms(nom,age):
    print (nom + " Dupont " + age)

noms("Martin","18")
noms("Camille","19")
noms("Paul", "12")

# arguments arbitraires
# dans le cas d'un nombre de parametres inconnu on ajoute une * avant le parametre, ceci retourne un tuple. Un "arg"
def youngest(*annees):
	print("le plus jeune a " + str((min(annees)))+" ans")
    
youngest(17,15,20,65,18,21,90)
# les paires key-value sont aussi disponibles
def fruits(couleur1, couleur2, couleur3):
    print("les cerises sont " + couleur1)

fruits(couleur1 = "rouges", couleur2="bleues", couleur3="vertes")
# de la meme facon si un nombre de clés est inconnu, **key, une "kwarg"
def voitures(**bagnole):
    print("c'est une "+ bagnole["marque"])
voitures(km=18756,marque="Toyota")

# argument par defaut 
def pays(country="Belgique"):
    print ("il vient de " + country)
    
pays("France")
pays()

# les listes et tuple sont des arguments valides.
# return est appliquable
def math(x):
    return x * 2
print(math(2))

# pass evite toujours les erreurs en cas de fonction vide

# récurssion mathématique, une fonction peut s'appeler elle même
def boucle(l):
    if l > 0:
        output = l + boucle(l - 1)
        print(output)
    else: 
        output = 0
    return output

boucle(6) # cette fonction fera 6 fois l + (l-1)

# Fonction Lambda
# fonction anonyme prenant un ou plusieurs arguments mais n'ayant qu'une expression

x = lambda a : a + 1 # ajoute 1 a x 
print(x(2)) # x = 2 + 1, cad 3  
# tres utile a l'interieur d'une fonction a inconnue 
def multip(n):
    return lambda b : b * n
multiplicateur = multip(3)  # variable indiquant par cb on multiplie
print(multiplicateur(6))    # multiplie b(multiplicateur/lambda) par n

