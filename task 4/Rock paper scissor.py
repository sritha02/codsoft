import random

# Initialize scores for the user and computer
user_score = 0
computer_score = 0

# Define a function to determine the winner of a round
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Main game loop
while True:
    print("\nRock, Paper, Scissors Game")
    print("Options:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")

    # Get user's choice
    user_choice = input("Enter your choice (1/2/3/4): ")

    if user_choice == '4':
        print("Thanks for playing!")
        break

    if user_choice not in ('1', '2', '3'):
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
        continue

    # Map user's choice to 'rock', 'paper', or 'scissors'
    choices = ['rock', 'paper', 'scissors']
    user_choice = choices[int(user_choice) - 1]

    # Generate a random choice for the computer
    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    # Update scores
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    print(f"User Score: {user_score}")
    print(f"Computer Score: {computer_score}")

    play_again = input("Do you want to play another round? (yes/no): ")
    if play_again.lower() != 'yes':
        print("Thanks for playing!")
        break
