num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
opre = input("Enter the oprater: ")
if opre == "+":
    print(num+num2)
elif opre == "-":
    print(num1-num2)
elif opre == "/":
    print(num1/num2)
elif opre == "*":
    print(num1*num2)
else:
    print("Invelid opreater")