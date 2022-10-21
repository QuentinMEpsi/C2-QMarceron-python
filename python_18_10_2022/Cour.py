print("Hello, World")
# ----------------------------------------------------------------------------------------------------------------------
if 5>2:
    print('pourquoi')
# ----------------------------------------------------------------------------------------------------------------------
x = 5 # Automatiquement le type INT
y = "Salut" # Automatiquement le type STRING
print(x)
print(y)
# ----------------------------------------------------------------------------------------------------------------------
"""
pour faire du commentaire
multiligne
"""
# ----------------------------------------------------------------------------------------------------------------------
# Casting :
a = str(5)
b = int(5)
c = float(5)
print(a)
print(b)
print(c)
# Afficher le type de la variable
print(type(a))
print(type(b))
print(type(c))
# ----------------------------------------------------------------------------------------------------------------------
# Déclarer une chaîne avec '' ou ""
d = "Vincent"
e = 'Artz'
# f = `voila` marche pas
print(d)
print(e)
# ----------------------------------------------------------------------------------------------------------------------
# une variable doit commencer par une letre
# ne peu pas démarrer par un nombre
# caractère alpha et l'underscore
# variable sensible à la case
# Camel case maVariable = "Vincent"
# Pascale case MaVariable = "Vincent"
# Snake case ma_variable = "Vincent"
# ----------------------------------------------------------------------------------------------------------------------
h, i, j = "Fruits", "Légumes", "Lait"
# h, i, j = "Fruits"
print(h)
print(i)
print(j)
print(h,i,j)
print(h+i+j)
# ----------------------------------------------------------------------------------------------------------------------
fruits = ["Pomme", "Banane", "Cerise"]
k, l, m = fruits
print(k)
print(l)
print(m)
# ----------------------------------------------------------------------------------------------------------------------
n = "génial"
def maFonction():
    global n
    n = "Superbe"
    print("Python est " + n)

maFonction()
print("Python est " + n)
# ----------------------------------------------------------------------------------------------------------------------
# Type de données
# str = chaine
# numeric = int, float, complex
# sequences = list, tuple, range
# Mapping Type = dict
# Set Types = set, frozenset
# Booléens = bool
# Binary = bytes, bytesarray, memoryview
# None Type : NoneType
# ----------------------------------------------------------------------------------------------------------------------
x = 5
print(type(x))
# list
x = ["fruits", "légumes"]
# tuple
x = ("fruits", "légumes")
# range
x = range(6)
# dict
x = {"nom": "Marceron", "Age": 24}
# set
x = {"fruits", "légumes"}
# booléen
x = True
# bytes
x = b"Salut"
x = bytearray(5)
# ----------------------------------------------------------------------------------------------------------------------
x = 1
y = 3.5
z = 1j
a = float(x)
b = int(y)
c = complex(x)
print(type(a), type(b), type(c))
# ----------------------------------------------------------------------------------------------------------------------
import random
print(random.randrange(1, 10))
# ----------------------------------------------------------------------------------------------------------------------
# module GUI
# Tkinter
# interface graphique en python
# alternative
# PyQT5/PySide2
# wxPython
# Kivy
# ----------------------------------------------------------------------------------------------------------------------
# Bibliothèque = collection de fonction er d'objet qui vont fournir des fonctionnalitées qui vont enrichir les capacités d'un langage
# math
# par exemple factorial

from math import factorial
print(factorial(5))
# ----------------------------------------------------------------------------------------------------------------------
# string multiligne
a = """Exemple voila,
on peu faire
plusieurs lignes
"""
print(a)
# ----------------------------------------------------------------------------------------------------------------------
a = "Hello, ça va"
print(a[5])
# ----------------------------------------------------------------------------------------------------------------------
for x in "Quentin":
    print(x)
# ----------------------------------------------------------------------------------------------------------------------
a = "Hello, ça va"
print(len(a))
# ----------------------------------------------------------------------------------------------------------------------
a = "Hello, ça va"
print("va" in a)
# ----------------------------------------------------------------------------------------------------------------------
a = "Hello, ça va"
if "va" in a:
    print("trouvé")

a = "Hello, ça va"
if "bah" not in a:
    print("pas trouvé")

a = "Hello, ça va"
if "va" in a:
    print("trouvé")
else:
    print("pas trouvé")
# ----------------------------------------------------------------------------------------------------------------------
x = "Salut les amis"
print(x[2:5])

x = "Salut les amis"
print(x[:5])

x = "Salut les amis"
print(x[5:])

x = "Salut les amis"
print(x[-5:-2])
# ----------------------------------------------------------------------------------------------------------------------
# Mettre la chaîne de caractères en majuscule/miniscule
a = "Hello world"
print(a.upper())
b = "VOILA"
print(b.lower())
# Eliminer les espaces vides avant et après la chaîne
a = " Bonjour ça va ? "
print(a.strip())
# Remplacer des éléments dans une chaîne de caractères
a = "Bonjour ça va ?"
print(a.replace("j", "o"))
# Transformer une chaîne de caractères en tableau par rapport à un caractère
a = "Bonjour, ça va ?"
print(a.split(","))
# Concaténation de chaîne
a = "Bonjour"
b = "toi"
ab = a + " " + b
print(ab)
# Combiner une chaîne de caractères avec une valeur numérique
age = 24
txt = "Voici mon age : " + str(age)
print(txt)

age = 24
age2 = 25
txt = "Voici mon age : {0}ans et je vais avoir {1}ans"
print(txt.format(age, age2))
# Caractère spéciaux
a = "Bonjour voici \"Le\" merveilleux langage"
print(a)
# Trouver la position d'un mot dans une chaîne de caractère
a = "Bonjour je m'appelle quentin"
print(a.find("je"))
# Trouver la position d'un mot dans une chaîne de caractère avec un intervalle
a = "Bonjour je m'appelle quentin"
print(a.find("je", 3, 6))
# ----------------------------------------------------------------------------------------------------------------------
class maClasse():
    def __len__(self):
        return 0
monObjet = maClasse()
print(bool(monObjet))
# ----------------------------------------------------------------------------------------------------------------------
# Opérateur Puissance
a = 2
b = a ** 10
print(b)
# ----------------------------------------------------------------------------------------------------------------------
malist = ["Pierre", "Julien", "Anne", "Marie", "Lucien"]
# Fusionner 2 list
malist.insert(2, "Vincent")
print(malist)
# Etendre une list
malist2 = ["Maxime", "Gary"]
malist.extend(malist2)
print(malist)
# Supprimer un élément par rapport à sont nom
malist.remove("Pierre")
print(malist)
# Supprimer un élément par rapport à sont index
malist.pop(2)
print(malist)
# Supprimer le dernière élément de la list
malist.pop()
print(malist)
# Supprimer un élément par rapport à sont index
del malist[0]
print(malist)
# Vider une list
malist.clear()
print(malist)
# ----------------------------------------------------------------------------------------------------------------------
fruit = ["Banane", "Pomme", "Kiwi", "Mangue"]
nouvelleList = []

# Méthode 1
for x in fruit:
    if "a" in x:
        nouvelleList.append(x)
print(nouvelleList)

# Méthode 2
fruit = ["Banane", "Pomme", "Kiwi", "Mangue"]
nouvelleList = [x for x in fruit if "a" in x]
print(nouvelleList)

# Méthode 3
fruit = ["Banane", "Pomme", "Kiwi", "Mangue"]
nouvelleList = [x for x in fruit if x != "Banane"]
print(nouvelleList)

# Méthode 4
nouvelleList = [x for x in range(5)]
print(nouvelleList)

# Méthode 5
nouvelleList = [x for x in range(20) if x < 10]
print(nouvelleList)

# Méthode 6
fruit = ["Banane", "Pomme", "Kiwi", "Mangue"]
nouvelleList = [x.upper() for x in fruit]
print(nouvelleList)

# Méthode 7
fruit = ["Banane", "Pomme", "Kiwi", "Mangue"]
nouvelleList = ["eau" for x in fruit]
print(nouvelleList)

# ----------------------------------------------------------------------------------------------------------------------
default_dict = {}
print(type(default_dict))

# ----------------------------------------------------------------------------------------------------------------------
# Customiser un sort
chaine = ["Pierre", "Julien", "Anne", "Marie", "Lucien"]
chaine.sort(reverse = True)
print(chaine)

def maFonct(n):
    return abs(n-50)

fruit = [100, 50, 87, 65, 82, 23]
fruit.sort(key = maFonct)
print(fruit)