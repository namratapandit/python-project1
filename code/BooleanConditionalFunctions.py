# Boolean Functions for simple arithematic functions

# simple arithematic functions with user input
# here we are using built-in input function for taking inputs from user
# we are also using built-in int function for convering (data type conversion ) to integer

def add(num1, num2):
    return num1 + num2

def sub(num1, num2 ):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2 ):
    return num1 / num2

def main():

    myName =input("Whats is your name?")
    print("Welcome " + myName)

    validvariable = False
    while not validvariable:
    try:
            print("Please enter 2 numbers :")
            num1 = int(input("Enter number1"))
            num2 = int(input("Enter number 2:"))
            operation = input("Please choose from the following operations: Add : 1, Subtract : 2, Multiple : 3, Divide: 4 , Exit:9 ")
            validvariable = True
    except:
            print("Invalid entries!")


    if operation == '1' :
        print("Adding...")
        print(add(num1, num2))
    elif operation == '2' :
        print("Subtracting...")
        print(sub(num1, num2))
    elif operation == '3':
        print("Multiplying...")
        print(mul(num1, num2))
    elif operation == '4' :
        print("Dividing...")
        print(div(num1, num2))
    elif operation == '9' :
        validvariable = False
        print("Thank you, Exiting from program!")
    else:
        print("Incorrect value")



main()