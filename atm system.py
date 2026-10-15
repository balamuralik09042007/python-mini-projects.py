print("=======ATM SYSTEM===========")
balanc=500


 print("1-withdraw")
 print("2-deposite")
 print("3-ckeck balance")
 print("4-exit")

 enter=input("enter the opition[1-4]:")

 if enter == "1":# te valu 1 are stored string in enter variable so to give it string
    amount=float(input("enter the amount:"))
    if amount <= balanc: 
        balanc-=amount
        print(balanc,"balance ammount")
    else:
        print("enter minimum ammount")
 elif enter == "2":
    amount=float(input("enter the amount:"))
    balanc+=amount
    print(balanc,"deposite successfully")
 elif enter == "3":
    print("your balance:",balanc)
 elif enter == "4":
    print("thank you you are exit")
 else:
    print("invalid opition give it coreect")
    break
    
    
