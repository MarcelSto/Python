#Start - Hotelbeispiel 2 (Beispiel 1 ist "iff bedingung.py")

zimmerpreis = float(input("Zimmerpreis? "))
aufenthaltsdauer = float(input("Dauer? "))
anzahl_kinder = int(input("Anzahl Kinder? "))

kinderpreis = 0
zaehler = 0

while zaehler < anzahl_kinder:    #zähle ich gleich runter und zaehler 0
    alter = int(input(f"Gebe jetzt an wie alt das Kind {zaehler+1} ist: "))

    if alter <=6:
        rabatt=100
    else:
        rabatt=50

    kinderpreis+=zimmerpreis*aufenthaltsdauer*(1-rabatt/100)        
    zaehler+=1                                                      

erwachsenenpreis=2*zimmerpreis*aufenthaltsdauer 
gesamtpreis=erwachsenenpreis+kinderpreis        

print("Angebot für diese wunderbare Familie von Herrn Klink")
print(f"\n Zimmerpreis Nacht und Person {zimmerpreis} € und Aufenthaltsdauer {aufenthaltsdauer} in Nächte und Preis für die komplette Familie {gesamtpreis: .2f}")
