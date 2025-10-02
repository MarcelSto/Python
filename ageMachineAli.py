#Start - learn functions


"""
if age 50 + print u r old else print u will get old 2
"""
def ageMachine(age: int)->None:
    if age >= 50:
        print("You r old!")
    elif age < 50: 
        print("You will get old 2!")

#Call Function
ageMachine(60)


"""
this function accept two intiger as Argument and add them
return result of summation
"""
#snake_case --> wir können es für variablen nutzen
def addTwoNumbers(num1:int, num2:int)->int:
    return num1 + num2

result = addTwoNumbers(5, 6)
print(f"Result is:{result}")


#End