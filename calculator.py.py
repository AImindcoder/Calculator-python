#Simple calculator
print("Simple calculator")
num1=float(input("Enter the first number "))
num2=float(input("Enter the second number"))
#Chose the operation
print("Chose operation")
print("1. Addittion(+)")
print("2. Subtraction(-)")
print("3. Multiflication(*)")
print("4. Divission(/)")
operator=input("Enter the operators +,-,* or/")
#Show the result
if operator=="+":
    print("result:", num1+num2)
elif operator=="-":
    print("result:", num1-num2)
elif operator=="*":
    print("result:", num1*num2)
elif operator=="/":
    if num2 !=0:
        print("result:", num1/num2)
    else:
        print("Erroe: Can't devided by zero")
        
