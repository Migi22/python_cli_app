'''This is the main logic for the mini quiz game'''

from .quiz_game_utils import load_highscores, save_highscores, load_questions


def quiz_game():
    print("\n\n==Mini Quiz Game==")

    # Loads the necessary files
    highscores = load_highscores()
    questions_pool = load_questions()

    # Loop for entering a user name
    while True:
        # Prompt the user to enter his name
        username = input("Please enter your username: ").strip

        # Check if the username variable is empty
        if username == "":
            print("Username cannot be empty. Please try again.")
            continue

        # Check if the username is already exist
        if username in highscores:

            # Prompt the user that the username entered already exit.
            print(f'\nUsername "{username}" is already exist.')
            
            # Prompt user to ask if use the username and overwrite the score or choose a different username
            is_overwrite = input(f'Do you want to overwrite the previous score of "{username}"? (Y/N) ').capitalize()
            
            # Checks the response and proceed accordingly
            if is_overwrite == "Y":
                break
            else:
                print("Please enter a different username.")
        else:
            break
        
    # Ask user to select 2 mode, 5 question quiz or 10 question quiz
    while True:
        # Display the quiz modes
        print("""
        \nChoose quiz mode:
              1. 5 randonm Questions
              2. 10 random Questions
        """)   

        # Prompt the user to choose what quiz mode to pick
        mode = input("Please select a game mode: ")

        # Checks the response and proceed accordingly
        if mode == "1":
            num_questions = 5
            break
        elif mode == "2":
            num_questions = 10
            break
        else:
            print("Invalid input. Please select between choices 1 and 2.")
        
    # Then the system will select random 10 questions in the 15 pool of questions
    
    # Display the questions and its choices
    # The system will record the correct and wrong answers of the user.

    # Display the result afterwards

    # Display if play again or not. If not proceeds to the menu of mini quiz game

