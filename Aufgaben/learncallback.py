#Start - Lerne Callback richtig anzuwenden in Python

def sag_hallo():                    #Definiere die Funktion die als Callback dienen soll
    print("Hallo!")                 #was die funktion ausführen soll

def fuehre_aus(callback):           #Definiere eine Funktion die eine andere Funktion als Parameter nimmt
    print("Ich mache etwas...")
    callback()                      # Das ist der Callback
    print("Fertig!")

#fuehre_aus(sag_hallo)               #Rufe die Funktion auf und übergebe die Callback-Funktion als Argument


'''
Aufgabe 1 - Schreibe eine Funktion namens ausführen(callback), die einfach die übergebene Funktion ausführt
            Dann schreibe zwei einfache Funktionen die "Hallo" und "Ciao" ausgeben und übergebe sie als Callback an die ausführen Funktion. 
'''

def hallo():
    print("Hallo")

def ciao():
    print("Ciao")

def ausfuehren(callback):
    callback()

#ausfuehren(hallo)
#ausfuehren(ciao)

'''
Aufgabe 2 - Schreibe eine Funktion bearbeite_namen(callback, name), die namen an die callback funktion übergibt in Klein- und Großbuchstaben.
'''
##Definieren was als Callback dienen soll
def klein(name):                    #Funktion die einen String in Kleinbuchstaben ausgibt
    print(name.lower())

def gross(name):                    #Funktion die einen String in Großbuchstaben ausgibt
    print(name.upper())

def main(callback, name):           #Funktion die eine Callback Funktion und einen Namen als Parameter nimmt
    callback(name)                  #Ruft die Callback Funktion mit dem Namen als Argument auf

main(klein, "Hans")                 #Funktion main wird aufgerufen mit der Callback Funktion klein und dem Namen "Hans"
main(gross, "Hans")                 #Funktion main wird aufgerufen mit der Callback Funktion groß und dem Namen "Hans"
