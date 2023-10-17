import random
random_number = random.randint(1, 30)
guess_count=0
 
while True:
    guess_number = int(input("Guess the number (between 1 and 30): "))
    guess_count += 1
    if guess_number < random_number:
        print("Pick a higher number")
    elif guess_number > random_number:
        print("Pick a lower number")
    else:
        print("You guessed the correct number!")
        break  # Exit the loop when the correct number is guessed

print(f"The correct number was {random_number} and you guessed it after {guess_count} guesses")
