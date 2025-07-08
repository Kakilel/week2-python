import random

def get_difficulty():
    print("Choose difficulty: easy / normal / hard")
    while True:
        choice = input("Enter difficulty: ").lower()
        if choice == "easy":
            return 10
        elif choice == "normal":
            return 7
        elif choice == "hard":
            return 5
        else:
            print("Invalid choice. Please choose: easy, normal, or hard.")

def give_hint(secret):
    if secret % 2 == 0:
        print("Hint: The number is even.")
    else:
        print("Hint: The number is odd.")
    if secret < 50:
        print("Hint: The number is less than 50.")
    else:
        print("Hint: The number is 50 or greater.")

def play_game():
    secret_number = random.randint(1, 100)
    attempts = get_difficulty()
    wrong_guesses = 0

    print("\nI'm thinking of a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it!\n")

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess == secret_number:
            print(" Correct! You guessed the number!")
            return
        elif guess < secret_number:
            print("Too low.")
        else:
            print("Too high.")

        attempts -= 1
        wrong_guesses += 1
        print(f"Remaining guesses: {attempts}")

        if wrong_guesses == 3:
            give_hint(secret_number)
        if attempts == 0:
            print(f"\n? Game Over! The number was {secret_number}.")

play_game()
