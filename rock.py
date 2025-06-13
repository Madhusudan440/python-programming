import random

def get_user_choice():
    options = {1: "rock", 2: "paper", 3: "scissors"}
    
    while True:
        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        try:
            choice_num = int(input("Enter your choice (1/2/3): "))
            if choice_num in options:
                return options[choice_num]
            else:
                print("Invalid input. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'win'
    else:
        return 'lose'

def display_result(user, computer, result):
    print(f"\nYou chose: {user.capitalize()}")
    print(f"Computer chose: {computer.capitalize()}")

    if result == 'tie':
        print("Result: It's a tie!")
    elif result == 'win':
        print("Result: You win! ")
    else:
        print("Result: You lose. ")

def play_again():
    while True:
        again = input("Do you want to play again? (y/n): ").strip().lower()
        if again in ['y', 'n']:
            return again == 'y'
        print("Invalid input. Please enter 'y' or 'n'.")

def main():
    print("=== Welcome to Rock-Paper-Scissors ===")
    user_score = 0
    computer_score = 0
    round_number = 1

    while True:
        print(f"\n--- Round {round_number} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        if result == 'win':
            user_score += 1
        elif result == 'lose':
            computer_score += 1

        display_result(user_choice, computer_choice, result)
        print(f"Score => You: {user_score} | Computer: {computer_score}")

        if not play_again():
            print("\nThanks for playing!")
            break

        round_number += 1

if __name__ == "__main__":
    main()
