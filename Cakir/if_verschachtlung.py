#Start - Wenn Verschachtlung

star_wars = ["Meister Klink","Yoda","Darth Vader","Leia Organa","Han Solo","Luke Skywalker","Mace Windu","Jar Jar Binks"]

#print("Darth Vader" in star_wars)

if "Darth Vader" in  star_wars:
    print("Ja er ist Böse aber nicht mehr lange")
else:
    print("Wahscheinlich ein Buchstabenfehler!")


if "Herr Cakir" in star_wars:
    print("Das were der Hammer")
else:
    print("Schade er ist nicht dabei")

###########################################################
text = "Ich bin ein Berliner"

if "ein" in text:
    print("bin da")
else:
    print("es gibt kein ein")

###########################################################

alter = 30

if not alter >=30:
    print("Ja ich bin nicht über 30")
else:
    print("Ich bin über 30")

if alter <30:
    print("Ich bin unter 30")

############################################################

pokemon = ["Enton","Glumanda","Glurak","Glutexo","Shiggy"]

if "Mewtwo" not in pokemon:         #hier wird explizit überprüft ob "Mewtow" NICHT in der Liste ist
    print("Schade nicht dabei")

if not "Mewtwo" in pokemon:         #
    print("Nicht Dabei bro, sorry")

