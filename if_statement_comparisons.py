num1 = input("Enter the first num: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")
def max_num():
    if num1>=num2 and num1>=num3:
        print("The give first number is greater then other number " + num1)
        #return num1 # we can use return function to print the value
    elif num2>=num1 and num2>=num3:
        print("The given seconde number is greater then other number " + num2)
       # return num2
    else:
        print("The give third number is greater then other number " + num3)
        #return num3
print(max_num())