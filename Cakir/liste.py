#Start - Einführung Liste in Python


###Join funktion

studenten = ["Jörg", "Patrick", "Holger", "Christopher", "Christian"]
print(studenten)

print(", ".join(studenten))
print("g ".join(studenten))         #join fügt "g" immer an das Ende der Wörter ein aus Jörg wird Jörgg

ausgabe = ", ".join(studenten)
print("Das sind meine liebsten Studenten "+str(ausgabe)+" nicht wahr?")




###Split funktion

students = "Jörg,Patrick,Holger,Christopher,Christian"
print(students.split(","))                                  #Split macht aus einem String eine Liste


###Split Function 2

stud = "Jörg,Patrick,Holger,Christopher,Christian"
ergebnis = stud.split(",")
print(ergebnis)
print(type(ergebnis))                       #Fragt den Datentyp ab

test = ["1", "2", "3", "4"]
print(test[2])                              #zeigt die 3. Stelle der Liste an 

tier = "Wer hat die Gans gestohlen"
print(tier.split(" "))


#Ende 