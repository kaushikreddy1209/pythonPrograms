import random
number=random.randint(1, 100)
guess = None
number_of_tries = 0
max_tries = 10
input("Welcome to the guessing game, You have 10 tries to guess the number right! Press any key to play")
while number_of_tries < max_tries: #Loop breaks if max_tries is reached
    try:
        guess=int(input("Guess: "))
        number_of_tries+=1
        if guess<number:
            print("you have guessed a number less than the Secret number!")
        elif guess>number:
            print("You have guessed a number greater than the Secret number!")
        else:
            print("You have guessed it right!")
            break
    except ValueError:
        print("Please enter a valid number!")

if number_of_tries == max_tries:
    print(f"You have reached your maximum number of tries. The secret number is {number}")