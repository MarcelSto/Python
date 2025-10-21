#Start
'''
Aufgabe Erstellen eine Anwendung namens Energieverbrauch. Definiere logische Variablen,
um den Energieverbrauch eines elektrischen Geräts für ein Jahr berechnen

    Info:
    o  In einem Haushalt gibt es 3 Fernseher a 1 kWh und es wird täglich 3h "Game of Thrones" geschaut.
       Jeden Tag!
    o  Wenn jemand kocht dann 4 mal die Woche. Herd verbraucht 2 kWh und das Gerät ist 2 Stunden im Betrieb!
    o  Telefon und Router sowie Rechner verbrauchen insgesamt 2 kWh und sind insgesamt 4 Stunden am Tag in Betrieb.
       Jeden Tag!
    o  Ein Familienmitglied ist "super sparsam" und benutzt eine elektrische Heizung 8 kWh, jeweils 20 h am Tag - 170 Tage im Jahr.


Berechne den Verbrauch und Strompreis, wenn 1 kWh 0,40 Euro kostet.   
'''

#Variablen 
strompreis = 0.40

verbrauch_Tv=3*1*3*365
verbrauch_Herd=4*2*2*52
verbrauch_Router=2*4*365
verbrauch_Heizung=8*20*170

gesamtverbrauch = verbrauch_Tv + verbrauch_Herd + verbrauch_Router + verbrauch_Heizung
                                    #0,40
stromkosten = gesamtverbrauch * strompreis

#Ausgabe
print(f"Der Gesamtverbrauch beträgt: {gesamtverbrauch} kWh")
print(f"Die Stromkosten betragen: {stromkosten:.2f} Euro")          #.2f = 2 Nachkommastellen



#Ende