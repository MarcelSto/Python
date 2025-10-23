#Start - If bedingung

'''
Schreiben Sie ein Programm,
das für eine Familie (zwei Erwachsene und ein kind) ein Angebot erstellt.
Kinder von 0 bis 6 Jahren übernachten kostenlos, ab 7 Jahren auch Erwachsene gibt es einen Rabatt
von 70% auf den Zimmerpreis pro Person und Nacht

    o Wenn Alter der Kinder kleiner 7, dann beträgt Rabatt 100%
    o Sonst 70% für alles andere 
Kinderpreis = Zimmerpreis x Aufenthaltsdauer x (1-Rabatt/100)

'''

##Variable
zimmerpreis = float(input("Geben Sie den Zimmerpreis pro Person und Nacht ein: "))
aufenthaltsdauer = int(input("Geben Sie die Aufenthaltsdauer in Nächten ein: "))
alter_kind = int(input("Gebe bitte das alter des Kindes ein: "))
rabatt = None
kinderpreis = None


##If abfrage
if alter_kind < 7:
    rabatt = 100
else:
    rabatt = 70

kinderpreis =  zimmerpreis*aufenthaltsdauer*(1-rabatt/100)

erwachsenenpreis = 2*zimmerpreis*aufenthaltsdauer

gesamtpreis = erwachsenenpreis+kinderpreis


##Programmaufruf
print(f"Gesamtpreis für die Familie beträgt: {gesamtpreis}")
