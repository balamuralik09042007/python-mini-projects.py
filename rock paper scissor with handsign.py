import random

rock= '''  
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor='''
    _______
---'   ____)____
          ______)
         ________)
      (____)
---.__(___)
'''
v=[rock,paper,scissor]

user_choose=int(input("what is your option,0 for rock,1 for paper,2 for scissor:"))

print("user_choose:",v[user_choose])

computer_choose=random.randint(0,2)

print("computer_choose:",v[computer_choose])

if user_choose == 0 and computer_choose ==2:
    print("you are win")
elif computer_choose ==0 and user_choose ==2:
    print("computer are win")
elif user_choose ==0 and computer_choose== 1:
    print("computer are win")
elif computer_choose ==0 and user_choose==1:
    print("computer are win")
elif user_choose ==1 and computer_choose == 2:
    print("computer are win")
elif computer_choose ==1 and user_choose == 2:
    print("you are win")
elif computer_choose == user_choose:
    print("match are draw")


