# simple function to add 2 numbers

def addfunction(num1, num2):
    """this is a comment for developer readibility"""
    print("The sum value is :")
    return num1 + num2

# another function main calling the addFunction function with arguments
def main ():
    print(addfunction(1,1))  #should return the sum value i.e. 2
    print(addfunction(5,4)) #should return the sum value i.e. 9
    print(addfunction(10, 10))  #should return the sum value i.e. 20

#calling the main function
main()


def StrinConcatFun():
    """" This function shows the string concatination doe using two variables"""
    str1 = "shashu"
    str2 = "namu"
    return "\n" + str1 + " " + str2

print(StrinConcatFun())