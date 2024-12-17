import random

def get_computer_choice():
    """Randomly select Rock, Paper, or Scissors for the computer."""
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)

def get_user_choice():
    """Get the user's choice and validate it."""
    user_input = input("Enter Rock, Paper, or Scissors: ").capitalize()
    while user_input not in ['Rock', 'Paper', 'Scissors']:
        print("Invalid choice. Please try again.")
        user_input = input("Enter Rock, Paper, or Scissors: ").capitalize()
    return user_input

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Main function to play the game."""
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Run the game
if _name_ == "_main_":
    play_game()