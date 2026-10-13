print("====smart expense analysis=====")

class analysis():
    
    def __init__(self):
        self.b={ "food":7000,
        "transport":2500,
        "medical":3000,
        "mobil reachare":1000,
        "enjoyment":2500}
        self.limited=15000
        self.buget=20000
    def total_expensces(self):
        total=sum(self.b.values())
        print("total",total)
        for name,value in self.b.items():
            print(f"{name}:{value}")
            
    def highest_limit(self):
        maxvalue=max(self.b ,key=self.b.get)
        print("highest spending:",maxvalue)
        print("limited_amount:",self.limited)
    
    def warning(self):
        total=sum(self.b.values())
        if total > self.limited:
            print(f"cross your limit:{total}")
        else:
            print(f"your balance:{total-self.buget}")
            
    def higestthree(self):
        v=sorted(self.b.items(),key=lambda item:item[1],reverse=True)
        for i,(name,value) in enumerate(v[:3],start=1):
            print(f"{i},{name}-4{value:,}")
        
    
    
v=analysis()
v.total_expensces()
print("============================================")
v.highest_limit()
v.warning()
print("===============================================")
v.higestthree()
