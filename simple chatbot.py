import datetime
import random
import string
while True:
    print("Hello! i am chatbot! how can help you?")
    print("i have only this commands")
    print("1-greetings(hi,hello)")
    print("2-todaydate")
    print("3-calculater")
    print("4-password(password generster")
    print("5-jokes")
    print("6-exit")
    print("===============================")
    user=input("type the command:")
    if user =="hello" or user=="hi" or user=="Hello" or user=="Hi":
        print("hi! how are you!")
        print("===================================")
    elif user == "todaydate" or user =="todaytime":
        todaydate=datetime.date.today()
        print("today date is:",todaydate)
        todaytime=datetime.datetime.now().strftime("%H:%M:%S")
        print("current time is:",todaytime)
        print("=====================================")
    elif user == "calculater":
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
        print("===============================================")
    elif user == "password":
        pasword=''.join(random.choices(string.ascii_letters+"@"+string.digits,k=8))
        print(" your password are:",pasword)
        print("=================================================")
    elif user == "jokes":
        joke1=["Friend: Dei, ava un story paathaala?"," Me: Paatha da!","Friend: Reply panninaala?"," Me: Illa da!Friend: Appo?",
              "Me:CCTV camera kooda namma veetta paakkum da… adhu namma relative aagiduma? 😭🤣"]
        for i in joke1:
            print(i)
        print("==================================================")
    else:
        if user=="exit":
            print("thanking you!")
            break
        
