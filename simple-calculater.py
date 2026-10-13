print("=========SIMPLE CALCULATOR============")
items = []
num = int(input("enter the number of items: "))

for i in range(1, num + 1):
    price = float(input(f"enter the price of item {i}: "))
    items.append(price)

total = sum(items)

if total >= 1000:
    discount = total * 0.25
else:
    discount = 0

final_bill = total - discount

print("total:", total)
print("discount:", discount)
print("final_bill:", final_bill)
