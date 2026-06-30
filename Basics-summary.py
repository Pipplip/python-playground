# -*- coding: utf-8 -*-
"""
Zusammenfassungen
"""

''' mehrzeiliger Kommentar '''
# einzelner Kommentar

# ===============================================================
#                          Datentypen
# ===============================================================
# Text Type: 	    str
# Numeric Types: 	int, float, complex
# Sequence Types: 	list, tuple, range
# Mapping Type: 	dict
# Set Types: 	    set, frozenset    Bsp: fs = frozenset({"apple", "banana", "cherry"})
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview
### mb = b"Hello" # bytes
### mba = bytearray(5) # bytearray
### mmv = memoryview(bytes(5))
# None Type: 	    NoneType
n = None

# ===============================================================
#                          None Type
# ===============================================================
# None ist ein spezieller Datentyp in Python, der einen Nullwert oder das Fehlen eines Werts repräsentiert.
# Es ist ein eigenständiger Typ namens NoneType und wird häufig verwendet, 
# um anzuzeigen, dass eine Variable keinen Wert hat oder dass eine Funktion nichts zurückgibt. 
# ===============================================================
nt = None
print(type(nt)) # <class 'NoneType'>

# ===============================================================
#                           Variablen
# ===============================================================
i = 42
j = 2.34
print(type(i)) # <class 'int'>
t = True
false = False

a , b, c = 1, 2.5, "Hallo" # Mehrfachzuweisung
print(a, b, c)  # 1 2.5 Hallo

g = h = 3 # Mehrfachzuweisung gleicher Wert
print(g, h)  # 3 3

# Operatoren:
# (+) Summe a + b
# (-) Differenz a - b
# (*) Produkt a * b
# (/) Quotient a / b
# (//) ganzzahlige Division a // b (abgerundet)
# (%) Modulo a % b
# (abs) Betrag von a abs(a)
# (**) Potenzieren a^b

# ===============================================================
#                        Strings
# ===============================================================
string1 = "Hallo"
print(string1[0]) # H
print(len(string1)) # 5

print(string1[1:5]) # slicing -> allo

# ===== Nützliche String Methoden, Beispiele =====
# strip() - entfernt Leerzeichen am Anfang und Ende
# lower() / upper() - macht alles klein / groß
# split() - teilt String in Liste auf (Standard: Leerzeichen)

# ===== format strings =====
age = 22
print(f"Ich bin {age} Jahre alt.")
# Aufruf einer Funktion in einem format string
def get_years(age=22):
    return age 
print(f"Ich bin {get_years(22)} Jahre alt.")

## Modifiers von format strings
# Dezimalstellen
number = 3.14159
print(f"Pi auf 2 Nachkommastellen: {number:.2f}") # Pi auf 2 Nachkommastellen: 3.14
# Padding
name = "Max"
print(f"Name mit Padding: {name:>10}") # Name mit Padding:        Max
# Binär, Oktal, Hexadezimal
num = 42
print(f"Binär: {num:b}, Oktal: {num:o}, Hexadezimal: {num:x}") # Binär: 101010, Oktal: 52, Hexadezimal: 2a

# ===============================================================
#                       print
# ===============================================================
name = "name"
age = 22
print(name + ":" + str(age))
print(name, ':', age)
print(f'{name} : {age}') # formatted string
print('%s : %s' % (name, age))
print('{} : {}'.format(name, age))

# ===============================================================
#                       Listen [a,b,c] - Arrays
# ===============================================================
# Listen = veränderbar also z.B. liste[0] = 1
# Listen sind geordnet, veränderbar, erlauben doppelte Einträge und besutzen indizes
# Werte können verschiedene Datentypen sein
# Arrays gibt es in Python nicht, stattdessen benutzt man Listen oder das Modul array
# ===============================================================
l1 = [3,99,"Ein Text"]
l2 = [ 42, 65, [45, 89], 88 ]
print(l2[2]) # [45,89]

# prüfen ob Liste leer ist
if not l1:
    print("Liste ist leer")

# Listen kopieren
l3 = ["a","b","c","d"]
l3copy1 = l3[:]
# oder
l3copy2 = list(l3)
# oder
l3copy3 = l3.copy()

# verschachtelte Listen kopieren
from copy import deepcopy
l5 = ["a","b",["ac","ad"]]
l6 = deepcopy(l5)

# zip-Funktion - Matrix erstellen
z1 = [11, 12, 13]
z2 = [21, 22, 23]
z3 = [31, 32, 33]
T = zip(z1, z2, z3)
print(list(T)) # [(11,21,31), (12,22,32), (13,23,33)]

# Liste auslesen
for entry in l3:
    print(entry)

for i in range(len(l3)):
    print(l3[i])

while i < len(l3):
    print(l3[i])
    i += 1  

# ===== List Comprehension =====
# Syntax:
# newlist = [expression for item in iterable if condition == True]
[print(entry) for entry in l3] # Auslesen einer Liste

newlist = [x for x in l3 if 'a' in x] # neue Liste mit Elementen die 'a' enthalten

# ===== List Methoden =====
# Stapelspeicher (stack) für Listen: Vorstellbar wie ein Bücherregal
# Auf Stapel legen (push/append), nehmen (pop) und schauen was ganz oben liegt (peek)
#    append() oder '+': am Ende des Stapels/Liste hinzufügen - append bevorzugen, da performanter // l3.append("e") oder l3 += ['e', 'f']
#    insert(): an beliebige Stelle des Stapels hinzufügen z.B. l3.insert(1, 'c') // füge an Index 1 -> 'c' hinzu. Index 1 wird nicht überschrieben
#    remove(): entfernen eines Elements z.B. l3.remove('b')
#    pop(): letzte Element nehmen und ausschneiden
#    pop(i): Element i nehmen und ausschneiden // Der Vorteil von pop() ist, dass wir als Rückgabewert den Inhalt des gelöschten letzten Listeneintrags bekommen und damit weiterarbeiten können 
#    extend(t): an eine Liste mehrere Elemente anhängen, z.B. eine weitere Liste // l3.extend(['e','f'])
#    index(): Gibt die Stelle des Elements im Stack zurück z.B. l3.index("c")
#    del(): löschen der Liste. z.B. del(l3)
#    count(): Gibt die Anzahl eines bestimmten Elements zurück z.B. l3.count("a")
#    len(): Gibt die Anzahl aller Elemente zurück z.B. len(l3)
#    clear(): löscht alle Elemente in der Liste z.B. l3.clear()
#    copy(): erstellt eine Kopie der Liste z.B. l3copy = l3.copy()
#    reverse(): dreht die Reihenfolge der Liste um z.B. l3.reverse()
#    sort(): sortiert die Liste z.B. l3.sort()
#    + : zwei Listen zusammenfügen z.B. l4 = l3 + ['e','f']
#    * : Liste mehrfach hintereinander anfügen z.B. l4 = l3 * 3
z3.append(34) # z3 = [31,32,33,34]

# Sortierung
stack5 = [6,8,7,3,8,4]
print(sorted(stack5)) # [3, 4, 6, 7, 8, 8]

# unpack
l7 = [1,2,3]
x, y, z = l7
print(x) # 1
print(y) # 2
print(z) # 3

if 2 in l7:
    print("2 ist in der Liste")

# ===============================================================
#                   Tupel (1,2,3,"Text")
# ===============================================================
# Tupel = unveränderbar, z.B. tupel[0] = 1 -> Exception
# Nur lesen erlaubt
# Tupel sind geordnet, unveränderbar, erlauben doppelte Einträge und benutzen indizes
# Werte in Tupeln können verschiedene Datentypen sein
# Iteration über Tupel und andere Funktionalität wie bei Listen
# ===============================================================
t1 = (3,99,"Ein Text")

# ===============================================================
#                       Dictionary
# ===============================================================
# Entspricht einer Map in Java: key-value mapping
# 
# Dictionaries sind veränderbar, ungeordnet, keine doppelten Einträge (keys müssen eindeutig sein)
# Die keys in einem Dictionary müssen unveränderbar (immutable) sein, z.B. Strings, Zahlen oder Tupel.
# Die Values können beliebige Datentypen haben und auch veränderbar sein.
# 
# map = {"key1":"value1","key2":"value2"}
# ===============================================================
map2 = {"key1" : "value1", "key2" : "value2", "key3" : "value3"}
map2["key3"] = "value3a" # value ändern
map2.get("key1") # value1
if "value1" in map2: # True
    print("enthalten")

# Schleife über Dictionary
for key in map2:
    print("key: ", key, "value: ", map2[key])

for key, value in map2.items():
    print("key: ", key, "value: ", value)

for val in map2.values():
    print("value: ", val)

for key in map2.keys():
    print("key: ", key)

# copy
map2copy = map2.copy()
# oder
map2copy2 = dict(map2)

# ===== Nested Dictionaries =====
map3 = {
    "person1": {"name":"Max", "age":22},
    "person2": {"name":"Anna", "age":23}
} # entspricht dict(key, dict(key,value))
print (map3["person1"]["name"]) # Max
nestedDic = map3["person2"]
print(nestedDic["age"]) # 23

# Schleife über nested dictionaries
for person, info in map3.items():
    print("Person: ", person)
    for key in info: # info ist wieder ein Dictionary
        print("  ", key, ": ", info[key])


# ===== Nützliche Methoden =====
# kopieren: map2.copy(), bei verschachtelter Dic. deepcopy
# dic.clear() - Dic leeren
# dic.get("key1") - liefert value zu key1
# dic.fromkeys(["key1","key2"], "defaultValue") - neues Dic mit keys und default value
# dic.items() - liefert alle key.value Paare
# dic.values() - liefert alle values
# dic.keys()  - liefert alle keys
# dic.pop("key1") - löschen eines keys
# dic.setdefault() - add key-value Paar (nur wenn noch nicht vorhanden)
# dic.update({"key3":"value3"}) - Dic wird erweitert oder überschrieben

# ===============================================================
#                       Sets
# ===============================================================
# Set: Mengen. Eine Sammlung von einzigartigen Elementen.
# Veränderliche Objekte wie Listen sind als Sets nicht erlaubt
# 
# Sets sind ungeordnet, veränderbar, keine doppelten Einträge
# 
# set = {'Stadt1','Stadt2'}
# ===============================================================

set1 = {'Hamburg','Müchnen','Frankfurt'}
set2 = set(('Paris', 'Paris', 'Lyon')) # mit Konstruktor

# ===== Nützliche Methoden =====
# set1.add('Stuttgart') - Elemente hinzufügen
# set.clear() - Set leeren
# set.copy() 
# set1.union(set2) - Vereinigung zweier Mengen (alle Elemente aus set1 und set2)
# set1.update(set2) - fügt alle Elemente von set2 in set1 ein
# set1.difference(set2) - Differenz zweier Mengen (set1 - set2 geht auch)
# set1.difference_update(set2) - entfernt alle Elemente einer Menge aus einer anderen Menge, die gleich sind
# set.discard("Stuttgart") oder set.remove("Stuttgart") - entfernen eines Elements
# set1.intersection(set2) - Liefert Schnittmenge zweier Sets (gleiche Elemente)
# set1.isdisjoint(set2) - True, wenn zwei Sets keine übereinstimmende Einträge haben (also leere Schnittmenge)
# set1.issubset(set2) - True, wenn Untermenge von set1 in set2 vorhanden ist
# set1.issuperset(set2) - True, wenn Obermenge von set1 in set2 vorhanden ist, x > y x enthält mindestens ein Element von y

# frozenset - unveränderbares Set
fs1 = frozenset({'A','B','C'})
# -> fs1.add('D') # führt zu Exception

# ===============================================================
#                       Verzweigungen
# ===============================================================
if a == b:
    print()
else:
    print()
# -----------
if c > d:
    print()
elif c == d:
    print()
else:
    print()

# short hand if: beispiel
x = 42
y = 24
min = x if x < y else y # Zuordnung je nach Bedingung
# dies ist das gleiche wie:
#if x < y:
#    min = x
#else:
#    min = y
print(min)

print("A") if x > y else print("B") # Kurzform if-else

# Assign values based on conditions
bigger = x if a > b else b

# ===== Operatoren =====
# == -> 42 == 42 True, [1,2]==[1,2] True
# != -> 42 != 43 True, {1,2] != 17 True
# < / > -> 4 < 12 True, "Ti" < "Tisc" True
# <= / >= -> 4 <= 4 True
# and, or, not -> Verbinden von Verknüpfungen

# ===== pass Statement - Platzhalter =====
# pass wird verwendet wenn eine Anweisung syntaktisch erforderlich ist, aber kein Code ausgeführt werden soll.
# z.B. in leeren Schleifen, Funktionen oder Klassen
if x > y:
    pass # Wenn nichts passieren soll

def f():
    pass # leere Funktion
# pass kann man vergleichen mit einem leeren Block {}

# match-case (wie switch-case in Java)
day = 2
match day:
    case 1:
        print("Montag")
    case 2:
        print("Dienstag")
    case 3 | 4 | 5:
        print("Mittwoch, Donnerstag oder Freitag")
    case _:
        # default
        print("Anderer Tag")

# ===============================================================
#                   Schleifen (while, foreach)
# ===============================================================
# while
i = 0
while i < 4:
    i += 1
    if i == 2:
        continue
    if i == 3:
        break

# foreach
languages = ["a","b"]
for lan in languages:
    print(lan)

# ===============================================================
#                       Funktionen
# ===============================================================

def sayHello(name):
    """ function prints 'sayHello' """
    return "Hello " + name

# default Parameter, wenn beim Aufruf nichts übergeben wird
def sayHello2(name="everybody"):
    return "Hello" + name

# mit expliziter Angabe des Rückgabetyps und der Parametertypen
def my_sum(val1: int, val2: int) -> int:
    return val1 + val2

# wenn man globale Variablen in einer Funktion benutzen will, muss man diese angeben
s = "Globaler String"
def f():
    global s
    print(s)
    s = "Globaler String verändert"
    print(s) # print: Globaler String verändert

# scopes - LEGB rule
x = "global"
def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)
outer()
print("Global:", x) # Inner: local, outer: enclosing, global: global

# Neben Parameter für Funktionen kann man auch Argumente *args und **kwargs benutzen
# wird verwenden wenn man nicht weiß wie viele Parameter übergeben werden
def func_with_args(title, *args, **kwargs):
    print("title: ", title) # normaler Parameter sind auch erlaubt
    for arg in args: # args ist ein Tupel
        print("arg: ", arg) # (1,2,3)
    for key in kwargs:
        print("key: ", key, "value: ", kwargs[key]) # kwargs ist ein Dictionary {name:"Max", age:22}

func_with_args(1,2,3, name="Max", age=22)

# ===== Decorators - Funktionen die andere Funktionen erweitern ======
def changeCase(original_function): # decorator function
    def wrapper_function(name):
        return original_function(name).upper()
    return wrapper_function

@changeCase # decorator anwenden
def display(name):
    return "Display function executed: " + name

print(display())

# ===============================================================
#                       Lambda Funktionen
# ===============================================================
# Lambda Funktionen = anonyme Funktionen
# Eine lambda Funktion kann beliebig viele Argumente annehmen, aber nur einen Ausdruck haben.
# Syntax: lambda argumente : ausdruck
# ===============================================================

x= lambda a, b : a + b
print(x(5, 3)) # 8

y = lambda s: s.upper()
print(y("hallo")) # HALLO

z = lambda s: s[0]
print(z("hallo")) # h

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11)) # 22

# Lambda functions are commonly used with built-in functions like map(), filter(), and sorted()
points = [1, 2, 3, 4, 5]
squared_points = list(map(lambda x: x**2, points))
print(squared_points) # [1, 4, 9, 16, 25]

# with filter
even_points = list(filter(lambda x: x % 2 == 0, points))
print(even_points) # [2, 4] 

# ===============================================================
#                          Rekursion
# ===============================================================
# Eine Funktion, die sich selbst aufruft
# 
# Eine Rekursive Funktion benötigt:
# 1. Basisfall (Abbruchbedingung)
# 2. Rekursiver Fall (Aufruf der Funktion mit verändertem Parameter)
# ===============================================================

def countdown(n):
  if n <= 0: # Basisfall
    print("Done!")
  else: # Rekursiver Fall
    print(n)
    countdown(n - 1)

countdown(5) 

# ===============================================================
#                       Generatoren
# ===============================================================
# Generatoren sind spezielle Funktionen, die einen Iterator zurückgeben.
# Sie ermöglichen es, Werte nacheinander zu erzeugen, anstatt alle auf einmal im Speicher zu halten.
# Dies ist besonders nützlich bei der Arbeit mit großen Datenmengen oder unendlichen Sequenzen.
# yield ist ähnlich wie return, aber anstatt die Funktion zu beenden, speichert es den aktuellen Zustand der Funktion und gibt den Wert zurück.
# ===============================================================
def my_generator():
    yield 1
    yield 2
    yield 3 

gen = my_generator()

for value in gen:
    print(value) # 1 2 3

# oder
gen2 = my_generator()
print(next(gen2)) # 1
print(next(gen2)) # 2
print(next(gen2)) # 3

# ===============================================================
#                           Range
# ===============================================================
"""
Eine range Funktion erzeugt eine Folge von Zahlen.
Return ist eine unveränderbare Sequenz von Zahlen, die häufig in for-Schleifen verwendet wird.
Syntax: range(start, stop, step)
- start: Anfangswert (inklusive). Standard ist 0.
- stop: Endwert (exklusive).
- step: Schrittweite. Standard ist 1.

"""
for i in range(0, 10, 2):
    print(i) # 0 2 4 6 8

for j in range(5): # start=0, step=1
    print(j) # 0 1 2 3 4

# Ranges sind immutable und nicht direkt anzeigbar, deshalb kann man sie in eine Liste umwandeln
print(list(range(3, 10, 3))) # [3, 6, 9]

r = range(1, 10, 2) # 1,3,5,7,9
print(6 in r) # False
print(len(r)) # 5

# ===============================================================
#                           Iterators
# ===============================================================
# Ein Iterator ist ein Objekt, das eine Sequenz von Werten durchlaufen kann.
# Ein Iterator implementiert die Methoden __iter__() und __next__().
# ===============================================================
"""
Lists, tuples, dictionaries, and sets sind alle iterable objects und können in einer for-Schleife verwendet werden.
Selbst Strings sind iterable objects.
Alle diese Objekte haben die Methode __iter__(), die einen Iterator zurückgibt.
"""
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

# wenn man eine eigene Klasse als Iterator verwenden will, muss man die Methoden __iter__() und __next__() implementieren
class MyNumbers:    
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x
  
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter)) # 1
print(next(myiter)) # 2

# ===============================================================
#                       Ausnahmebehandlung
# ===============================================================

try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())

except IOError as err:
    (errno, strerror) = err.args
    print("I/O error ({0}): {1}".format(errno, strerror))
except ValueError:
    print("No valid int value.")
except:
    (type, value, traceback) = sys.exc_info()
    print("Type: ", type)
    print("Value: ", value)
    print("traceback: ", traceback)
finally:
    print("Ich werde immer ausgegeben.")

# Throw einer Exception
x = -1
if x < 0:
  raise Exception("Sorry, keine Zahlen kleiner als 0 erlaubt") 

# ===============================================================
#                          Klassen
# ===============================================================
"""
Alle Klassen in Python erben von Object
__init__ entspricht dem Konstruktor
__del__ entspricht einem Destruktor (werden selten benutzt, weil man sich um das Aufräumen nicht kümmern muss)
__str__ und _repr__ entspricht dem toString in Java. Wandelt Datentyp in Sting um.
Diese Methoden kann man ueberschreiben. Und bei print() wird diese Methode dann aufgerufen

name   -> public - ohne führende Unterstriche
_name  -> protected - Bedeutet soviel wie "sollte nicht verwendet werden"
__name -> private - von aussen nicht sichtbar/benutzbar

statische Attribute (static in Java) = Klassenattribute (Eigenschaften, die für die ganze Klasse gelten und nicht nur für ein Objekt)
Wird unter der Klassendefinition deklariert. Hier Gesetze(...) oder counter
Statische Methoden sind an eine Klasse gebunden und nicht an eine Instanz

Felder werden in Python nicht deklariert, sondern bei der Initialisierung in __init__ erstellt.
Diese sind immer public und können von aussen verändert werden.
Beispielaufruf:
r = Roboter("Robo1", 2000)

self ist ähnlich wie this in Java und verweist auf die aktuelle Instanz der Klasse.
Wenn eine Methode z.B. ein Feld der Klasse verändern will, muss self davor stehen.
Beispiel:
def AendereName(self, name):
    self.name = name

Self steht in jeder Methodendeklaration als erster Parameter, damit die Methode auf die Instanz zugreifen kann.

Im Gegensatz zu z.B. Java werden Felder in Python nicht deklariert, sondern erstellt, wenn sie zum ersten Mal in einer Methode (meistens __init__) zugewiesen werden.
Felder sind Klassenattribute, die von allen Instanzen der Klasse geteilt werden, oder Instanzattribute, die nur für eine bestimmte Instanz gelten.

"""

# from robots import Roboter # importieren einer Klasse Roboter von Datei robots.py
class Roboter:

    __counter = 0 # private static
    Gesetze = ("Ich bin ein Klassenattribut", "...") # kann von allen Instanzen verwendet werden
    # Aufruf: print(Roboter.Gesetze)
    # print(Roboter.AnzahlRoboter())

    def __init__(self, name, baujahr): # entspricht dem Konstruktor: __init__ muss so bleiben
        self.name = name
        self.__baujahr = baujahr # Baujahr ist private
        type(self).__counter += 1

    def __del__(self): # Destruktor (kann man weglassen)
        print("Roboter wurde zerstört")
        type(self).__counter -= 1

    def SageHallo(self): # Methoden-Deklaration, statt self kann man auch this oder etwas anderes nehmen
        print("Hallo, ich bin " + self.name)

    def AendereName(self, name):
        self.name = name

    def GetName(self):
        return self.name

    def SetzeBaujahr(self, baujahr):
        self.__baujahr = baujahr

    @staticmethod
    def AnzahlRoboter():
        return Roboter.__counter

    
    # repr = Darstellung von Daten, aus dem String lässt sich wieder ein Objekt machen, bei str nicht
    # mit eval lässt sich daraus wieder eine Instanz machen
    def __repr__(self):
        return "Roboter (\"" + self.name + "\", "+ str(self.__baujahr) + ")"

    def __str__(self):
        return "Name: " + self.name

# ===== Vererbung =====
# class Marken_Roboter(Roboter): # in Python können Klassen von mehreren Klassen erben z.B. class Marken_Roboter(Roboter, Gattung)
class Marken_Roboter(Roboter):
    def __init__(self, name, baujahr, marke):
        super().__init__(name, baujahr) # Aufruf des Konstruktors der Oberklasse
        self.marke = marke

# main Aufrufe
if __name__ == "__main__":
    x = Roboter("Robo1", 2000)
    x.SageHallo()
    print(x) # repr oder str wird in KLasse gesucht und ausgegeben. Hier self.name
    neu = eval(repr(x))
    print(Roboter.AnzahlRoboter()) # 2
    del(neu)
    print(Roboter.AnzahlRoboter()) # 1
    print(Roboter.Gesetze)

    # Vererbung Beispiel
    mr = Marken_Roboter("MarkenRobo", 2020, "MarkeX")
    mr.SageHallo()
    print(mr.marke)

# ===============================================================
#                       Module
# ===============================================================
"""
Module sind Dateien mit Python Code, die Funktionen und Klassen enthalten. Eine Art Code-Bibliothek.
Module können in anderen Modulen oder Skripten importiert und wiederverwendet werden.
Module kann eine Sammlung von Funktionen, Klassen und Variablen sein, die thematisch zusammengehören.

Beispiel:
# mymodule.py
def greet(name):
    return "Hello, " + name

# main.py
import mymodule
# oder
from mymodule import greet
# oder
import mymodule as mm

print(mymodule.greet("Alice"))

Neben Funktionen, Klassen können auch Variablen in Modulen definiert werden.
Und in einem anderen Modul importiert und verwendet werden.

"""
import math
print(dir()) # listet alle eingebauten Module auf
print(dir(math)) # listet alle Funktionen und Attribute des Moduls math auf
print(help("math")) # Hilfe zu einem Modul
print(help("os")) # Hilfe zu einem Modul

# ===============================================================
#                       DateTime Modul
# ===============================================================
import datetime

x = datetime.datetime.now()
print(x) # aktuelles Datum und Uhrzeit
print(x.year) # Jahr

y = datetime.datetime(2018, 6, 1) # bestimmtes Datum erstellen
print(y)
# Formatieren von Datum und Uhrzeit mit strftime()
print(y.strftime("%B")) # Monat Name
print(y.strftime("%Y-%m-%d")) # Jahr-Monat-Tag
print(y.strftime("%A")) # Wochentag
print(y.strftime("%H:%M:%S")) # Stunde:Minute:Sekunde
# viele mehr ...

# ===============================================================
#                         JSON
# ===============================================================
"""
Python hat ein eingebautes Modul namens json, um mit JSON-Daten zu arbeiten.
"""
import json

# ===== Von JSON zu Python =====
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# Ergebnis ist ein Python dictionary:
print(y["age"]) 

# ===== Von Python zu JSON =====
x2 = {"name": "John", "age": 30,"city": "New York"}
y2 = json.dumps(x2) # covert into JSON string
print(y2)
# dumps hat viele optionale Parameter wie z.B. Einrückung und andere Formatierungen
# Beispiel mit Einrückung
y3 = json.dumps(x2, indent=4)

# ===== JSON Datei einlesen =====
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)

# ===== JSON Datei schreiben =====
with open('data2.json', 'w') as f:
    json.dump(x2, f)

# ===============================================================
#                RegEx - Reguläre Ausdrücke
# ===============================================================
import re
# Suche nach dem Muster "ai" in "The rain in Spain"
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) # <re.Match object; span=(5, 7), match='ai'>
# Suche nach allen Wörtern die mit "S" beginnen
x2 = re.findall(r"\bS\w+", txt)
print(x2) # ['Spain']
# Ersetze alle Leerzeichen mit "9"
x3 = re.sub(r"\s", "9", txt)
print(x3) # The9rain9in9Spain
# Teile den Text an jedem Leerzeichen
x4 = re.split(r"\s", txt)
print(x4) # ['The', 'rain', 'in', 'Spain']

# ===============================================================
#                   Arbeiten mit Dateien
# ===============================================================
# Datei = Daten + Kartei
#
# Inhalt einer Datei ist aus einer eindimesionalen Anneinanderreihung von Bits,
# die normalerweise in Byte-Blöcke zusammengefasst interpretiert werden.
# Bytes erhalten erst durch Anwendungsprogramme und das Bestriebssystem eine Bedeutung.
#
# modes: r (read), w (write), a (append), r+ (read and write), b (binary), t (text, default)
# ===============================================================

# Datei öffnen und lesen
# close wird bei "with open" nicht gebraucht
with open("lorem.txt", "r") as f:
    content = f.read()
    print(content)

# Text aus Datei lesen
# Beispiel Datei: lorem.txt
fobj = open("lorem.txt", "r")
for line in fobj:
    print(line.rstrip()) # rstrip() entfernt Zeilenumbruch
fobj.close()

# auf Datenstruktur speichern
lorem = open("lorem.txt").readlines()

# in String speichern
loremString = open("lorem.txt").read()

# Schreiben in eine Datei
input = open("lorem.txt", "r")
output = open("lorem2.txt", "w")
counter = 0
for line in input:
    counter += 1
    output_line = "{0:>3s} {1:s}\n".format(str(counter),line.rstrip())
    output.write(output_line)
input.close()
output.close()

# einfacher
with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

# Eine Datei löschen
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
    print("Die Datei existiert nicht")

# Verzeichnis löschen
os.rmdir("myfolder") # nur leere Verzeichnisse

# ===============================================================
#                   Threads / Locks & Coroutines
# ===============================================================
"""
MultiThreading = für GUIs, I/O. Shared memory. Python verwaltet Threading
Multiprocessing = eigener CPU Kern und Speicherbereich (schneller als Threading). System verwaltet Processing

ACHTUNG: wenn man Threads locked und alle auf einen anderen Thread warten hat man einen Deadlock

Threads:
- echte OS-Threads
- laufen parallel bzw. nebenläufig vom Betriebssystem gesteuert
- du brauchst Synchronisation (Locks etc.)

asyncio (Coroutines):
- ein Thread
- keine echte Parallelität
- Aufgaben wechseln sich kooperativ ab (await)
- gesteuert vom Event Loop

"""

# Beispiel Threading
import threading

class MyThread(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self) # Oberklasse von Thread aufrufen
        self.id = id
        self.name = name

    def run(self):
        lockMe.acquire() # blockiert bis der erste Thread fertig ist
        print("Starte ", self.id)
        print("Beende ", self.id)
        lockMe.release()

lockMe = threading.Lock()

t1 = MyThread(1,"t1")
t2 = MyThread(2,"t2")
t1.start()
t2.start()

# t1.join() # warten bis t1 fertig ist
# if t1.isAlive(): # gibt aus ob der Thread noch existiert
print("Beende Main")

# Beispiel Coroutines
import asyncio

async def task(name):
    print(f"{name} startet")
    await asyncio.sleep(2)
    print(f"{name} fertig")

async def main():
    await asyncio.gather(
        task("A"),
        task("B"),
        task("C")
    )

asyncio.run(main())
# hier laufen alle drei Tasks parallel, obwohl nur ein Thread verwendet wird

# ===============================================================
#                       Eingaben - User Input
# ===============================================================
# Eingaben: Eingabe wird immer als String interpretiert. Type-cast möglich
# ===============================================================

# Einfache Eingabe
eingabe = input("Ihre Eingabe? ")
# Eingabe casten
ein1 = int(input("Ihr Alter? "))
print(ein1)
print(type(ein1)) # <class 'int'>

# Eingabe von Listen
liste = eval(input("Liste? "))
# EIngabe z.B. ["rot","grün"]
print(liste)

# ===============================================================
#                Persistente Speicherung
# ===============================================================

# Pickle - Serialisierung von Objekten in Dateien
import pickle
# Speichern
#cities = ["Berlin", "Amsterdam", "München"]
#fh = open("serializedData.pkl","wb")
#pickle.dump(cities, fh)
#fh.close

# laden
fo = open("serializedData.pkl","rb")
staedte = pickle.load(fo)
fo.close
print(staedte)

# Shelve - ähnlich wie ein Bücherregal
# Das Regal ist eine Datei und die Bücher sind unsere Daten
# Empfohlen bei Dictionaries
import shelve
s = shelve.open("MyShelve") # wenn es die Datei nicht gibt, wird diese angelegt
s["street"] = "main street"
s["city"] = "London"

for key in s:
    print(key)

s.close()

# ===============================================================
#           Umwandlung in exe Datei mit PyInstaller
# ===============================================================
"""
Install: pip install pyinstaller
In Konsole pyinstaller datei.py

Zusätzlich:
pip install auto-py-to-exe

Danach in Console:
auto-py-to-exe
"""

# ===============================================================
#                       GUI: Modul tkinter
# ===============================================================
"""
tkinter - wird mit Python bereits geliefert, muss nicht extra installiert werden
"""
import tkinter as tk

root = tk.Tk()

w = tk.Label(root, text="Hello Tkinter!")
w.pack()

root.mainloop()


# ===============================================================
#                           Modul OS 
# - um auf Betriebssystem Funktionen zuzugreifen, z.B. Dateien in einem Pfad auflisten
# ===============================================================
import os

print(os.name) # Ausgabe BS: nt = Windows, posix 0 = Linux, Mac
print(os.getcwd()) # Arbeitsverzeichnis auslesen
print(os.environ) # Systemvariablen auslesen
print(os.listdir()) # Inhalt des Verzeichnisses ausgeben
os.rmdir(Pfad) # Verzeichnis löschen
os.remove(Datei) # Datei löschen
print(os.path.isfile('datei.pdf')) # prüfen ob Datei
print(os.path.isdir('datei.pdf')) # prüfen ob Verzeichnis
os.rename() # umbenennen

# ===============================================================
#                           Modul  PIP
# ===============================================================
# Version prüfen: pip --version
# Installierte Packages anzeigen: pip list
# Hilfe: pip help
# Upgrade: python -m pip install --upgrade pip
# Downgrade: python -m pip install pip==18.0 (or any other version)
# Packages installieren z.B.: pip install numpy
# Packages updaten: pip install --upgrade numpy
# Packages deinstallieren: pip uninstall <package_name>