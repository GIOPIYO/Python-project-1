import random

while True:
    play_again = input("Do you want to play a number guessing game? (y/n): ").lower()
    if play_again != 'y':
        break 

    # Player chooses the difficulty level
    player_level = input("Enter the your level (Easy, Medium, Hard): ").lower()

    if player_level not in ["easy", "medium", "hard"]:
        print("Invalid difficulty level. Please choose easy, medium, or hard.")
        continue


    if player_level == "easy":
        random_number = random.randint(1, 15)
        max_attempts = 6
    elif player_level == "medium":
        random_number = random.randint(1, 30)
        max_attempts = 9
    elif player_level == "hard":
         random_number = random.randint(1, 45)
         max_attempts = 12
    else:
        print("Invalid difficulty level. Please choose easy, medium, or hard.")
    

    guess_count = 0

 #Player inputs the guesses
    while guess_count < max_attempts:
        guess_number = int(input("Guess the number (between 1 and 45): "))
        guess_count += 1
        
        if guess_number < random_number:
            print("Pick a higher number")
        elif guess_number > random_number:
            print("Pick a lower number")
        else:
            print("You guessed the correct number!")
          # Exit the loop when the correct number is guessed

     #to show the correct answer and result
    if guess_number==random_number:
       print(f"The correct number was {random_number} and you guessed it after {guess_count} guesses")
    else:
        print(f"Out of guesses. The correct number was {random_number}.")

print("Thanks for playing!")
