import random 

def entry():
    value = input("add a number between 0 and 500: ")
    if value.isdigit() and (int(value)>=0 and int(value)<=500):
        return value
    else:
        print("please put a valid number")
        return entry()

def get_random_value():
    value = random.randint(0,500)
    return value

def check_value(random_value,user_input):
    if int(user_input) > int(random_value):
        print( "choose a smaller number")
        return True
    elif int(user_input) < int(random_value):
        print("choose a bigger number")    
        return True
    else:
        print("you find the value congratulation !!!!")
        return False


def main():
    test = True
    i = 4
    random_value = get_random_value()
    while test:
        i-=1
        user_input = entry()
        if(check_value(random_value,user_input)):
            print(f"you have {i} chances left")
            if i == 0 :
                print(f"the value is {random_value} you lose run the app to play again")
                break    
        else:
            break
main()            