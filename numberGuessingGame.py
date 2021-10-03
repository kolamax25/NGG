import random


comN = random.randint(1,9)

chances = 5

while chances!=0:
    humN = int(input("Guess a number from 1-9: "))
    
    if humN <= 0 or humN > 9:
        print("Not a valid number")

    else:


        if humN == comN:
            print("Congrats you guessed correctly")
            chances = 0
        
        if humN < comN:
            print("You have ", chances, " chances left. The Number is too low try again:")
            chances = chances - 1

        if humN > comN:
            print("You have ", chances, " chances left. The Number is too high try again:")
            chances = chances - 1


if chances == 0 and humN != comN:
    
    print("No more chances left. The correct answer is ", comN)