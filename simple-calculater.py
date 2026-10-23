num1=int(input("enter the 1st number:"))
num2=int(input("enter the 2nd number:"))
operator=input("enter your operators(+,-,*,/,%,//):")

if operator == "+":
    print("your value is:",num1+num2)
elif operator =="-":
    print("your value is:",num1-num2)
elif operator =="*":
    print("your value is:",num1*num2)
elif operator =="/":
    print("your value is:",num1/num2)
elif operator =="%":
    print("your value is:",num1%num2)
elif operator =="//":
    print("your value is:",num1//num2)
else:
    print("ivalid syntex")
