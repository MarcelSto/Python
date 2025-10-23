#Start- Saw-Quiz
from random import randint

print(f"Willkommen bei Saw, ein tödliches Zahlenrätsel")
print(f"Du hast 5 versuche, die richtige Zahl zwischen 1 und 10 zu erraten")
print(f"Wenn du es nicht schaffst, wirst dua uf die grasamste Weise was ein Autor sich ausdenken kann eliminiert \U0001F608")

random_number=randint(1,10)
attempts=5

while attempts >0:
    input_value = input(f"Gebe eine Zahl zwischen 1 und 10 ein, du hast aktuell {attempts} frei") 

    if input_value.isdigit():
        input_value = int(input_value)
        if 1<= input_value <=10:
            if input_value==random_number:
                print("-----------------------------------------------------")
                print("Du hast Gebonnen!(ദ്ദി˙ᗜ˙) ")
                print("-----------------------------------------------------")
                break
            else:
                attempts-=1
                if attempts>0:
                    print("Falsch, Try again! ⎛⎝( ` ᢍ ´ )⎠⎞ᵐᵘʰᵃʰᵃ")
                else:
                    print("-----------------------------------")
                    print("Tja nix Gebonnen")
                    print("Bischt am Arsch Ehy!")
                    print(f"Korrekte Nummer war {random_number}")
        else:
            print("Bischt du Dumm?")
            attempts-=1
    else:
        print("Zahlen! Bicht du Dumm? ಠ_ಠ ")
        attempts-=1
print("War Geil!")