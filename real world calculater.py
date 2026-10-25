print("=====REAL WORLD CALCULATER======")
num1=int(input("enter the 1st number:"))
while True:
    operation=input("enter the option(+,-,/,//,%,exit):")
    num2=int(input("enter the next number:"))
    if operation =="+":
        num1=num1+num2
        print("result is:",num1)
    elif operation =="-":
        num1=num1-num2
        print("result is:",num1)
    elif operation =="/":
        if num2==0:
            print("zero are not divisable")
        else:
            num1=num1/num2
            print("result is:",num1)
    elif operation =="//":
        if num2==0:
            print("zero are not divisable")
        else:
            num1=num1//num2
            print("result is:",num1)
    elif operation =="%":
        num1=num1%num2
        print("result is:",num1)
    elif operation == "exit":
        print("final result is:",num1)
        print("calculater are closed!!!")
        break
    else:
        print("invalid number")
