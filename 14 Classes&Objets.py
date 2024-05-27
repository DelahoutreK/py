# une classe est un constructeur d'objet, un recette
# un objet est l'instance d'une classe, un produit de la recette

class Couleur(): # une classe
    x = "rouge"
p1 = Couleur() # l'obet instancié depuis la classe
print(p1.x)

# typiquement on utilisera une fonction __init__ pour déclarer une classe
class Eleves:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
eleve1 = Eleves("Paul",30)
print(eleve1.nom + str(eleve1.age))