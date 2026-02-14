print("simple calculator")
try :
    num1 = int(input("enter first number:"))
    operator = input("enter operator ( + , - ,* , / )")
    num2 = int(input("enter second number:"))

    if operator == "+" :
        print("Result = ", num1 + num2 )
    elif operator4 == "-":
        print("Result = ", num1 - num2 )
    elif operator == "*":
         print("Result = ", num1 * num2 )
    elif operator == "/":
        if num2 != 0:
             print("Result = " , num1 / num2 )
        else:
             print("num2 cannot be zero" )

    else:
        print("invalid output")

except :
    print("please enter valid operator")
