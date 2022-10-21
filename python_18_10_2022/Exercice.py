# EXERCICE 1
prenom = str("Pierre")
nom = str("Jaques")
age = int(20)
majeur = bool(True)
compte_en_banque = float(20135.384)
amis = ["Marie", "Julien", "Adrien"]
parents = ("Marc", "Caroline")

print("Nom Prenom : " + nom + " " + prenom + "\nMajeur ? " + str(majeur) + " " + str(age))
print("Somme : " + str(compte_en_banque))
print("Amis : " + str(amis))
print("Parents : " + str(parents))

# -----------------------------------------------------------------------------------------------------------------------
# EXERCICE 2
nombre1 = 15
nombre2 = "15"
nombre3 = str(15)
print("Le nombre est " + str(nombre1))
print("Le nombre est " + nombre2)
print("Le nombre est " + nombre3)

# -----------------------------------------------------------------------------------------------------------------------
# EXERCICE 3
a = 2
b = 6
c = 3
print(a, b, c, sep=" + ")
print(str(a) + " + " + str(b) + " + " + str(c))

# -----------------------------------------------------------------------------------------------------------------------
# EXERCICE 4
list1 = range(3)
list2 = range(5)
# list est un mot réservé donc il faut renommer list en list1 ou autre
print(list(list2))

# -----------------------------------------------------------------------------------------------------------------------
# EXERCICE 5
prenom = "Pierre"
# Methode 1
if type(prenom) is str:
    print("La variable est une chaîne de caractère")
else:
    print("ce n'est pas une chaîne de caractère")

# Methode 2
if type(prenom) == str:
    print("La variable est une chaîne de caractère")
else:
    print("ce n'est pas une chaîne de caractère")

# Methode 3
if isinstance(prenom, str):
    print("La variable est une chaîne de caractère")
else:
    print("ce n'est pas une chaîne de caractère")

# Methode 4
if isinstance(prenom, str):
    print("La variable est une chaîne de caractère")
elif isinstance(prenom, int):
    print("La variable est un entier")
else:
    print("Autre")

# -----------------------------------------------------------------------------------------------------------------------
# EXERCICE 6
a = "Bonjour je m'appelle Gary, Je répète Bonjour"
b = a.replace("Bonjour", "Bonsoir")
print(b)
a = "Bonjour je m'appelle Gary, Je répète Bonjour"
b = a.replace("Bonjour", "Bonsoir", 1)
print(b)

# -----------------------------------------------------------------------------------------------------------------------
# EXERCICE 7
chaine = "Pierre, Julien, Anne, Marie, Lucien"
filteredChaine = chaine.split(",")
filteredChaine.sort()
print(filteredChaine)
print(sorted(filteredChaine))

# -----------------------------------------------------------------------------------------------------------------------
# EXERCICE 8
from math import pi
rayon = 10
volume = (((4/3)*pi)*rayon)**3
print('Le volume de la sphere est ', volume, 'cm3')

# -----------------------------------------------------------------------------------------------------------------------
# EXERCICE 9
# a = int(input("Valeur : "))
import random
a = random.randrange(1, 20)
print(a)

if type(a) is int:
    if int(a) > 10:
        print("Supérieur à 10")
    elif int(a) == 10:
        print("Egale à 10")
    else:
        print("Inférieur à 10")
else:
    print("Ce n'est pas un nombre")

# -----------------------------------------------------------------------------------------------------------------------
# EXERCICE 10
num1 = 5
num2 = 15
numlist = []
while (num1 <= num2):
    numlist.append(num1)
    num1 += 1
print(numlist)