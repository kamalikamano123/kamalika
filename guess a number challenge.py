import random
print("guess a number game")
print("guess a number between 1 to 50")
answer=random.randint(1,50)
print("Enter your guess:")
guess=0
while(guess!=answer):
    guess=int(input())
    if(guess<answer):
        print("Your guess is lower")
    elif(guess>answer):
        print("Your guess is higher")
print("Hurray! your guess is right the number is",answer)
