num1 = int(input("Enter the no. :"))
num2 = int(input("Enter the no. :"))
operator = input("Enter the operator(+,-,/,*):")
if operator == "+":
    print("Result =",num1+num2)
elif operator == "-":
    print("Result =",num1-num2)
elif operator == "*":
    print("Result =",num1*num2)
elif operator == "/":
    print("Result =",num1/num2)
else:
    print("Invalid Operator")                