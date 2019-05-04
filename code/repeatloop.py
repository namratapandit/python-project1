# program to take 2 numeric inputs and and operation selection from user
# the program repeats until the user does not exit
# Perform operations like add, sub, mul, divide
# keep repeating till user exits
# also handle exceptions for invalid inputs

def main():
    validinput = False
    # while loop runs till valid entries are entered
    while not validinput:
        try:
            num1 = int(input("Enter number1"))
            num2 = int(input("Enter number 2:"))
            operation = int(input("Please choose from the following operations: Add : 1, Subtract : 2, Multiple : 3, Divide: 4. Exit: 9 "))
            # ones valiinput values are taken, below operations are carried out based on the selection
            if operation == 1 :
               print("Adding...")
               print(num1 + num2)
            elif operation == 2 :
               print("Subtracting...")
               print(num1 - num2)
            elif operation == 3 :
               print("Multiplying...")
               print(num1 * num2)
            elif operation == 4 :
               print("Dividing...")
               print(num1 / num2)
            elif operation == 9 :
               print("Thank you, exiting program now!")
               validinput = True
            else:
                print("Wrong selection, try again")
        except:
            print("Invalid entries, try again! ")

main()