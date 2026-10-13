print("=========SIMPLE CALCULARER============")
V=[]
num=int(input("Enter the number of itemss:"))
for i in range(1,num+1):
  price=float(input("enter the price of item:"))
  V.append(price)

  total=sum(V)
if total >= 1000:
   discount=total*0.25
else:
   discount=0

final_bill=total-discount

print("total:",total)
print("discount:",discount)
print("finall_bill:",final_bill)
  
       
