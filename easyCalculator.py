#Start - simple Calculator

#Function Calculator
def calculator():
    num1 = float(input("Enter first number: "))         #define varables
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    if operator == '+':                                 #define Operator
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2    
    elif operator == '*':
        result = num1 * num2        
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"
    if result == int(result):                           #check if result is int or float
         result = int(result)
    elif result == float(result):
            result = float(result)
    print(f'The result is: {result}')                   #print result
    again = input("Next Operation? (yes/no): ")         #ask user if he want to do another operation
    if again == "yes":
         calculator()
    elif again == "no":                             
            print("Goodbye!")
        
         
        

#Operation result
calculator()
        
#End        

