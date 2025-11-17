#Start - Black Friday sales automat

liste = ["item0", "item1", "item2", "item3", "item4", "item5", "item6", "item7", "item8", "item9"]

def sales():
    print("Verfügbare Artikel:")
    for i, item in enumerate(liste):
        print(f"{i}: {item}")
    rabatt = input("Pick Item (Enter number 0-9): ")
    if rabatt.isdigit() and 0 <= int(rabatt) < len(liste):
        ausgewählt = liste[int(rabatt)]
        print(f"Danke für Ihre Bestellung! Ihr Produkt ist: {ausgewählt}")
    else:
        print("Ungültige Eingabe. Bitte geben Sie eine Zahl zwischen 0 und 9 ein.")

sales()
