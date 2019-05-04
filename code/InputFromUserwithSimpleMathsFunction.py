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
    print("Please enter 2 numbers :")
    num1 = int(input("Enter number1"))
    num2 = int(input("Enter number 2:"))
    print(add(num1, num2))
    print(sub(num1, num2))
    print(mul(num1, num2))
    print(div(num1, num2))

main()