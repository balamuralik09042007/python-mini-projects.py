print("--------CHECK THE PASWORRD STRONG OR WEEK--------")
pasword=input("enter your password:")

length=len(pasword)>=8
upper=any(i.isupper() for i in pasword)
lower=any(i.islower() for i in pasword)
digit=any(i.isdigit() for i in pasword)
special=any( not i.isalnum() for i in pasword)
# isalum is used to find any special charater  
# isalum any special character in object it return flase.so using not
print("length:",length)
print("upper:",upper)
print("lower:",lower)
print("digit:",digit)
print("special:",special)

if length and upper and lower and digit and special:
    print("your pasword is strong")
else:
    print("your paswor is week")
