#Start - Caesarkryptographie in Python


#Variables and Lists
Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




###Function to encrypt
def encrypt()->str:
    klartext = input("Enter the text you want to encrypt:")
    key = int(input("Enter the key: "))
    print("it is encrypted from " + klartext + " with key " + str(key))

###Function to decrypt
def decode()->str:
    encrypttext = input("Enter the text you want to decrypt:")
    key = int(input("Enter the key: "))
    print("it is decryptet from " + encrypttext + " with key " + str(key))



#Main Programm Funktion
def main():
    result = ""
    print("Hello, my name is Caesar, a enc and dec app!")
    userchoice = input("If u want to decrypt press d or if u want to encrypt press e:")


    if userchoice == "e":
        result = encrypt()
    elif userchoice == "d":
        result = decode()
    else:
        print("Wrong input.")
        main()
        
    return result



#Programm start
if __name__ == "__main__":
    main()