import random
import string
print("==========BANK MANAGEMENT SYSTEM=========")

print("===>option 1 for create a accout")
print("===>option 2 for deposit")
print("===>option 3 for withdraw")
print("===>option 4 for getting loan ")
print("===>option 5 for exit")

option = int(input("enter the your option:"))

if option == 1:
    age=int(input("enter your age:"))
    if age >=18:
        name=input("name:")
        adharnumber=input("adharnumber:")
        address=input("address:")
        fathername=input("fathername:")
        acc_num=random.randint(10000000,99999999)
        print(name)
        print(adharnumber)
        print(address)
        print(address)
        print("your account number is:",acc_num)
    else:
        print("sorry,you are under 18 not aligeble!!!")
elif option ==2:
    accountnumber=int(input("enter your account number:"))
    if  10000000 < accountnumber < 99999999:
        nname=''.join(random.choices(string.ascii_letters,k=10))
        print("your name is:",nname)
        amount=int(input("enter the amount:"))
        balance=5000
        if amount>100:
            balance+=amount
            print("your balance:",balance)
        else:
            print("please,enter above 100 rupes!!!")
    else:
        print("enter your account number correctly!!!")
elif option ==3:
    accountnum=int(input("enter your account number:"))
    if 10000000 <accountnum<99999999:
        namee=''.join(random.choices(string.ascii_letters,k=10))
        print("your name is:",namee)
        amoount=int(input("enter your amount:"))
        balancee=5000
        if amoount>100 and amoount<=balancee:
            balancee-=amount
            print("your balance is:",balancee)
        else:
            print("enter above 100 and amount is high")
    else:
        print("enter your account number correctly!!!")
elif option == 4:
    nameee=input("enter your name:")
    acountnumm=int(input("enter your account number:"))
    age=int(input("enter your age:"))
    print("your name:",nameee)
    print("your account number:",acountnumm)
    print("your age :",age)
    if age>18:
        print("you are aligible for loan!!")
        print("we only give education and house loan only!! ")
        print("education loan only 2 laks")
        print("house loan only 10 laks")
        print("E for education loan")
        print("H for house loan")
        your_option=input("enter your option:")
        if your_option =="E":
            rate=int(input("enter your amount:"))
            monthly_rate=rate/(12*50)*100
            print("monthly emi is:",f"{monthly_rate:.0f}")
        elif your_option =="H":
            rate=int(input("enter your amount:"))
            monthly_rate=rate/(12*500)*1000
            print("monthly emi is:",f"{monthly_rate:.0f}")
        else:
            print("give the correct option!!!")
elif option==5:
    print("your are exit")
else:
    print("invalid option")

