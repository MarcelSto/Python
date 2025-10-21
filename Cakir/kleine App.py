#Start - fake Subwayapp

print("Please, Enter youre username")
username = input()      #Benutzereingabe

print("Please, Enter youre password")
password = input()      #Passworteingabe

print("Registrierung erfolgreich bei subway :D")
print("---------------------------------------")

#Login
print("Please, enter username to login")
input_username = input()

#if Bedingung wenn das und das ist dann führe das hier aus 
if input_username == username:
    print("Allright, Username correct")
    print("Please, enter youre password now")
    input_password = input()
    if password == input_password:
        print("Login succsesfully")
    else:
        print("Invalid Password")
else:
    print("Inkcorrect Username")


#Ende