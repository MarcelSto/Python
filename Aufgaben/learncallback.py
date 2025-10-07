#Start - Lerne Callback richtig anzuwenden in Python
'''
Eine Callback-Funktion in Python (und in vielen anderen Programmiersprachen) ist eine Funktion,
die als Argument an eine andere Funktion übergeben wird, um später aufgerufen (zurückgerufen) zu werden - daher der Name „Callback“.
Das Prinzip basiert auf höherwertigen Funktionen: In Python können Funktionen wie Variablen behandelt werden - sie können übergeben, gespeichert und zurückgegeben werden.
'''

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

#main(klein, "Hans")                #Funktion main wird aufgerufen mit der Callback Funktion klein und dem Namen "Hans"
#main(gross, "Hans")                #Funktion main wird aufgerufen mit der Callback Funktion groß und dem Namen "Hans"

'''
Aufgabe 3 - Schreibe eine Funktion rechne(operation, a, b), die zwei Zahlen und eine Callback Funktion als Parameter nimmt.
'''
##Callback definieren
def addiere(a, b):                  #Funktion die zwei Zahlen addiert
    print("Resume is:", a + b)

def subtrahiere(a, b):              #Funktion die zwei Zahlen subtrahiert
    print("Resume is:", a - b)

def multipliziere(a, b):            #Funktion die zwei Zahlen multipliziert
    print("Resume is:", a * b)

def dividiere(a, b):                #Funktion die zwei Zahlen dividiert
    if b != 0:
        print("Resume is:", a / b)
    else:
        print("Division durch Null ist nicht erlaubt")
        return None

##def main function
def rechne(operation, a, b):        #Funktion die eine Callback Funktion und zwei Zahlen als Parameter nimmt || "operation" ist die Callback Funktion
    return operation(a, b)          #Ruft die Callback Funktion mit den zwei Zahlen als Argumente auf


#Ausführen der Funktion mit verschiedenen Operationen

rechne(addiere, 5, 3)               #Erwartet 8
rechne(subtrahiere, 5, 3)           #Erwartet 2
rechne(multipliziere, 5, 3)         #Erwartet 15
rechne(dividiere, 5, 2)             #Erwartet 2.5
rechne(dividiere, 5, 0)             #Erwartet Fehlermeldung                        