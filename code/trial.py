# simple calculator
# program incomplete

def add (num1 , num2):
    try:
        return int(num1) + int(num2)
    except:
         print("Invalid arguments")


def main():
    print("Welcome!")
    num1 = input("Enter number1: ")
    num2 = input("Enter number2: ")
    print(add(num1, num2))

main()