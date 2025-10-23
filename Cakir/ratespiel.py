#Start - Zahlenraten

import random



print("Geben sie eine Zahl zwischen 1 bis 5 ein: ")
input_value = input()

if input_value.isdigit():
    input_value = int(input_value)
    random_number = random.randint(1,5)
    if input_value == random_number:
        print("You Win! Nice!")
    else:
        print("Oh man D: You Lost youre House!")
else:
    print("Enter a Number! Idiot!")


print("Thank You for Playing in our Casino! See you soon :D!")


#Ende