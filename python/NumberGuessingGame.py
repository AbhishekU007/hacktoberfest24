import random


def choose_difficulty():
    print("🎮 Welcome to the Number Guessing Game! 🎮")
    print("Let's pick a difficulty level for you!")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")

    while True:
        choice = input("Please enter your choice (1/2/3): ")
        if choice in ['1', '2', '3']:
            if choice == '1':
                print("Great choice! The range will be from 1 to 10.")
                return 10
            elif choice == '2':
                print("Awesome! You'll be guessing a number between 1 and 50.")
                return 50
            elif choice == '3':
                print("Challenge accepted! The number will be between 1 and 100.")
                return 100
        else:
            print("Oops! That’s not a valid choice. Please select 1, 2, or 3.")


def play_game(max_number):
    secret_number = random.randint(1, max_number)
    attempts = 0
    max_attempts = 5

    print(
        f"\nI've picked a number between 1 and {max_number}. Can you guess it? You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < 1 or guess > max_number:
                print(f"Please guess a number within the range (1 to {max_number}). Let's try again.")
                continue

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                return attempts

        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    print(f" Sorry, you've used all your attempts. The secret number was {secret_number}.")
    return attempts


def main():
    total_score = 0

    while True:
        max_number = choose_difficulty()
        attempts = play_game(max_number)

        if attempts < 5:
            score = 5 - attempts
            total_score += score
            print(f"🌟 You scored {score} points! Total Score: {total_score}")
        else:
            print(f"💔 You scored 0 points. Total Score: {total_score}")

        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"😊 Thank you for playing! Your final score is: {total_score}. Have a great day!")
            break


if __name__ == "__main__":
    main()
