# if else, elif, else 

"""py
if(condition):
    action
elif(condition):
    action
else:
    action
"""

# Short hand statements
"""py
if condition: action else action
"""

# quand un bloc de code ne peut pas etre vide utiliser pass
"""py
if condition:
    pass
"""

# Boucle while
# tant qu'une condition est vraie, la boucle while continuera de tourner
i = 1 
while i < 10 : 
    print(i)
    i += 1   
# utiliser un break dans un bloc de code stoppera ce bloc
# utiliser un continue permet de continuer l'iteration d'un bloc de code, exemple
j = 0
while j < 10:
    print(j)
    j+= 1
    if j == 6:
        continue
    print(j) # notre output sera 1-2-3-4-5-7-8-9-10
# une boucle while peut aussi utiliser else

# Boucle for
# pour itérer sur une sequence quelconque (tuple, sets, lists, arrays en tout genre)
colors = ['#000000',"#999999","#222222"]
for a in colors:
    print(a)
# si appliqué a une string, for enumèrer les lettres de la string 
# break causera encore une fois la fin de la boucle
# continue sautera l'iteration concernée 
# possibilité d'utiliser range(), else et pass
