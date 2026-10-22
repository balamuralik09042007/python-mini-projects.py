print("====== SHOPE  BILLING SYSTEM======")
v=[]
num=int(input("enter the number of items:"))
for i in range(1, num+1):
    product=float(input("enter the items:"))
    v.append(product)
    total=sum(v)
    
if total >=1000:
    discount=total*0.25
else:
    discount=0

finall_bill=total-discount
print("total:",total)
print("discount:",discount)
print("finall biil:",finall_bill)
