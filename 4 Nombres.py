<<<<<<< HEAD
# int, un nombre simple positif ou negatif, sans limite, sans virgule

# float, un nombre simple spositif ou negatif, sans limite avec ou sans une virgule
# déclarable via la notation scientifique tel que: x = 20e5

# complexe, un nombre imaginaire déclaré tel que x = 4j
# le j indique la partie imaginaire: x = 3 + 4j

# conversion de type

a = 2
b = 2.2
c = 2j

# de int a float
x = float(a)

# de float a int
y = int(b) # tout apres la virgule est perdu!

# de int a complexe
z = complex(a)

# un complexe ne peut pas etre converti en int ou float

# Random Number, pas de fonction pour faire ca, il faut IMPORTER un module "random"
import random 
=======
# int, un nombre simple positif ou negatif, sans limite, sans virgule

# float, un nombre simple spositif ou negatif, sans limite avec ou sans une virgule
# déclarable via la notation scientifique tel que: x = 20e5

# complexe, un nombre imaginaire déclaré tel que x = 4j
# le j indique la partie imaginaire: x = 3 + 4j

# conversion de type

a = 2
b = 2.2
c = 2j

# de int a float
x = float(a)

# de float a int
y = int(b) # tout apres la virgule est perdu!

# de int a complexe
z = complex(a)

# un complexe ne peut pas etre converti en int ou float

# Random Number, pas de fonction pour faire ca, il faut IMPORTER un module "random"
import random 
>>>>>>> 221797b3f7397187369c1a66c82e768c350a3a1e
print(random.randrange(1,100))