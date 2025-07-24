
import random
import time

def choose_level():
    print("Choose a difficulty level:")
    print("1. Easy (1 - 10)")
    print("2. Medium (1 - 100)")
    print("3. Hard (1 - 1000)")
    level = input("Enter 1, 2, or 3: ")
    if level == '1':
        return 1, 10
    elif level == '2':
        return 1, 100
    elif level == '3':
        return 1, 1000
    else:
        print("Invalid choice. Defaulting to Medium.")
        return 1, 100

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    low, high = choose_level()
    secret_number = random.randint(low, high)
    attempts = 0
    start_time = time.time()

    while True:
        guess = input(f"\nGuess the number between {low} and {high} (or type 'exit' to quit): ")

        if guess.lower() == 'exit':
            print(f"The number was {secret_number}. Goodbye!")
            break

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("📉 Too low! Try again.")
        elif guess > secret_number:
            print("📈 Too high! Try again.")
        else:
            end_time = time.time()
            duration = round(end_time - start_time, 2)
            score = max(100 - attempts * 5, 0)
            print(f"\n🎉 Correct! You guessed the number in {attempts} attempts.")
            print(f"⏱️ Time taken: {duration} seconds")
            print(f"🏆 Your score: {score}/100")
            break

if __name__ == "__main__":
    number_guessing_game()
