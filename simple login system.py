print("====SIMPLE LOGIN SYSTEM=======")

stored_username=("Bala@123")
stored_password=(9042007)
print("below enter the username")
username=input(">>enter the username:")
print("below enter the password")
try:
    password=int(input(">>enter the password:"))
    if stored_username == username and stored_password == password:
       print("login succesfully")
    else:
        print("enter the correct username and password")
except:
    print("type only integer in password")
