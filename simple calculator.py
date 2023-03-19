select = int(input("select operations for 1,2,3,4:"))
number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))

# This function adds two numbers
def sum(number1,number2):
    return number1+number2

# This function subctracts two numbers
def substraction(number1,number2):
    return number1-number1
# This function multiplys two numbers
def multiplication(number1,number2):
    return number1*number2
# This function divides two numbers
def division(number1,number2):
    return number1/number2
if select==1:
    print(number1,"+",number2,"=",
          sum(number1,number2))
elif select==2:
    print(number1,"-",number2,"=",
          substraction(number1,number2))
elif select==3:
    print(number1,"*",number2,"=",
          multiplication(number1,number2))
elif select==4:
    print(number1,"/",number2,"=",
          division(number1,number2))
else:
    print("invalid input")