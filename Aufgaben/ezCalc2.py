#Start - Easy Calculator 2.0

#Function Next Operation
def again(): 
        answer = input("Next Operation? (yes/no): ")         #ask user if he want to do another operation
        if answer == "yes":
         calc() 
        elif answer == "no":                             
            return "Goodbye!"
        else:                       #catch all for invalid input
            print("Invalid Input, please try again")
            again()


#Function Calculator
def calc():
    print("Welcome to Easy Calculator 2.0")
    operation = input("Enter your Operation(e.g. 1+1): ")  #define varable input | define variable input as string (cant convert 1+1 to float) 

    result = None                                 #define variable result as None (to avoid errors) 

    if "+" in operation:
        numpart = operation.split("+") #split the input at the operator | variable.split() function splits a string into a list where each word is a list item result[0] + result[1]
        result = float(numpart[0]) + float(numpart[1])  #set variable "result" to numpart[0]+numpart[1] | convert the string to float
    elif "-" in operation:
        numpart = operation.split("-")
        result = float(numpart[0]) - float(numpart[1])  
    elif "*" in operation:
        numpart = operation.split("*")
        result = float(numpart[0]) * float(numpart[1])
    elif "/" in operation:
        numpart = operation.split("/")
        if float(numpart[1]) != 0:                        #check if the user is trying to divide by 0
             result = float(numpart[0]) / float(numpart[1])
        else:
             print("Error: Division by 0")     
    
    
    if result is not None:
         if result.is_integer():                        #check if the result is an integer
             result = int(result)                        #convert the float to an integer
    
    print(f"The result is: {result}")                  #print the result
    
    again()


    
#Operation result
calc()


#End