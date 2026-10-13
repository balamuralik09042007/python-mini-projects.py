print("===mail slicer====")

email=input("enter your email:")

index=email.index("@")

username=(email[:index])
domain=(email[index:])

print(f"the username is {username} and domain is {domain}")
