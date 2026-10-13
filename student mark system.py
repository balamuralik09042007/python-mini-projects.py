name=input("enter the student name:")
print("student name:",name)

tamil=int(input("enter the tamil mark:"))
english=int(input("enthe the english mark:"))
maths=int(input("enter the maths mark:"))
science=int(input("enter the science mark:"))
social=int(input("enter the social mark:"))

print("-------------------------------------------------------------------")

total=tamil+english+maths+science+social

average= total/5

print("total mark:",total)
print("average:",average)

print("-------------------------------------------------------------------")

if total >=90:
    print("grad A")
elif total >= 80:
    print("grad B")
elif total >= 70:
    print("grad C")
elif total >= 60:
    print("grad D")
else:
    print("fail")
    
