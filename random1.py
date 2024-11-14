import random
# random return 0<= number<1
#print("welcome to the virtual coin toos game")
#input("press Enter to start .....")
#random_number = random.randint(0,1)
#### print("Tails")
print("""
Welcome to the Coin Guessing Game!
Choose a method to toss the coin:
1. Using random.random()
2. Using random.randinit()
""")

choice = int(input("Enter your choice (1 or 2) :"))
if choice == 1 :
    if random.random()>=0.5 :
        randam_result = "tails"
    else :
         randam_result = "heads"

elif choice==2:
    if random.randint(0,1)==1 :
         randam_result = "tails"
    else :
         randam_result = "heads"
else  :
    print("invalid choice. please select either 1 or 2") 

choice_user = input("Enter Guess  heads/Tails").lower()

if choice_user==randam_result :
    print("congratulation! you won!")
else :
    print("sorry , you lost")

print(f"the computer's coin toss result was: {randam_result}")