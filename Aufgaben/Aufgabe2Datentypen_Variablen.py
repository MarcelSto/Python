#Aufgabe 2 - Datentypen/Variablen 

#Aufgabe 1) Deklarie 3 Namen, Alter, Höhen Variablen mit bel Wert

#Namen
name1 = "Marcel"
name2 = "Tim"
name3 = "Erdal"

#Alter
alter1 = 27
alter2 = 28
alter3 = 29

#Höhe in Meter
höhe1 = float(1.74)
höhe2 = float(1.86)
höhe3 = float(2.08)

#Aufgabe 2) Deklariere 2 Variablen vom Typ float L + B Rechteck --> Fläche Berechnen

a = float(4.5)
b = float(7.3)
c = float(a*b) #c=32.85

print(c)

#Aufgabe 3) Dekl. und Init. Variable für int(alter); float(Temperatur); string(Haustiername); bool(draußen regen=true)

Alter = int(27)
Temperatur = float(17.8)
Haustier = "Rolex"
Regen = True

print(f"{name1} ist {Alter} und sein Kater heißt {Haustier} und sagt jemand scheiß wetter heute ist seine Antwort {Regen}")

#Aufgabe 4) Addiere 2 intiger; Flächeninhalt eines Kreises; string1 + string2

#Addieren
Zahl1 = 5
Zahl2 = 4
Summe = Zahl1+Zahl2

print(Summe)

#Kreisfläche A= pi*r² Potenz in Python 2² = 2**2
import math
radius = float(2.43)

A = math.pi*radius**2

print(A)


#String1+String2
String1 = "Heute ist ein"
String2 = "schöner Tag"

print(f"{String1} {String2}")


