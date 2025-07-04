num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sign = input("Enter sign: ")
if sign == "+":
    print(num1+num2)
elif sign == "-":
    print(num1-num2)
elif sign == "*":
    print(num1*num2)
elif sign == "/":
    if num2 != 0:
        print(num1/num2)
    else:
        print("Error")
else:
    print("Invalid sign")