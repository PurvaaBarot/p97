import random
print("Number guessing name")
number = random.randint(1,9)
chance=0
print("guess  a number (between 1 and 9):")

while chance < 5:
    guess = int(input("Enter your guess : "))

    if guess == number:
        print("Congratulation you won")
        break
    elif guess<number:
        print("Guess a little higher number")
    else :
        print("Guess a little lower number")

        chance += 1

    if not chance < 5 :
        print("You lose . The number is" , number)
            
        

