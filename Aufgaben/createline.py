#Start - Create line 



##Function
def createLine(length):
    i = 0
    while i < length:                   #während länge größer als i print *
        print("*", end="")
        i += 1                          #i ist am anfang der schleife bei 0 und rechnet nach jedem * print +1 damit die schleife eine ende hat 
    print()

#createLine(24)


def createlines(länge):
    i = 0
    while i < länge:
        if i % 2 == 0:                  #Wenn Zahl durch 2 teilbar dann print * wenn nicht print -
            print("*", end="")
        else:
            print("-", end="")
        i += 1                          # i += 1 ist das leiche wie i = i +1
    print()                             #Das leere print sorgt für einen Zeilenumbruch beim aufruf der funktion

#createlines(12)
#createlines(9)


def stern(zeilen):
    i = 1
    while i <= zeilen:
        print("*" * i)
        i = i + 1

stern(5)

def sterne(lines):
    i = 1
    while i <= lines:
        if i % 2 == 0:
            print("-" * i)
        else:
            print("*" * i)
        i += 1

sterne(6)