#Start - callback example; customer in restaurante put order and waiter diliver food

 

def checkexistence(food_name:str)->bool:
    arr_foods = ["pizza", "pasta", "Döner"]
    arr_length = len(arr_foods)
    print(f"we have {arr_length} different foods on our menu.")

    if food_name in arr_foods:
        return True
    else:
        return False

def orderfood(food_name:str, checkexistence):
    is_food_exist = checkexistence(food_name)
    if is_food_exist:
        print(f"your {food_name} deliver soon.")
    else:
        print(f"sorry we don't have {food_name} on our menu.")
    
        
        





#-- actual programm use upper defined methods --#
order_string = input("What food would you like to order? ")
orderfood(order_string, checkexistence)  