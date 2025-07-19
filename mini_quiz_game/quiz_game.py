'''This is the main logic for the mini quiz game'''

import random
import emoji_util
from .quiz_game_utils import load_highscores, save_highscores, load_questions


def quiz_game():
    print("\n\n==Mini Quiz Game==")

    # Loads the necessary files
    highscores = load_highscores()
    questions_pool = load_questions()


    while True: # Loop for prompting the user to do another round of game or no
        while True:  # Loop for entering a user name
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
        selected_questions = random.sample(questions_pool, num_questions)

        correct_score = 0 # Tracks the correct answer
        wrong_score = 0 # Tracks the wrong answer
        
        # Display the questions and its choices
        # The system will record the correct and wrong answers of the user.
        for i, question_data in enumerate(selected_questions, str=1):
            print(f"\nQuestion {i}: {question_data['question']}")

            #display choices as A, B, C, D
            choices = question_data['choices']
            choice_labels = ['A', 'B', 'C', 'D']
            for label, choice in zip(choice_labels, choices):
                print(f" {label}. {choice}")
            
            # Get the user answer
            while True:
                user_input = input("Your answer (A/B/C/D): ").strip().upper()
                if user_input in choice_labels:
                    break
                else:
                    print("Invalid input. Please enter A, B, C, or D only.")
            
            selected_choice = choices[choice_labels.index(user_input)]

            # Check if correct
            if selected_choice == question_data['answer']:
                print(f"{emoji_util.CHECK} Correct!")
                correct_score += 1
            else:
                wrong_score += 1
                print(f"{emoji_util.CROSS} Wrong! Correct answer is: {question_data['answer']}")

        # Display the result afterwards
        print(f"\n Congratulations! You got {correct_score} out of {num_questions} correct.")

        # record the result(name and score of the user) to the json file
        # Update highscores
        if username in highscores:
            highscores[username]["total_correct"] += correct_score
            highscores[username]["total_wrong"] += wrong_score
            highscores[username]["total_games"] += 1
        else:
            highscores[username] = {
                "total_correct": correct_score,
                "total_wrong": wrong_score,
                "total_games": 1
            }

        # Save highscores
        save_highscores(highscores)

        # Play again?
        while True:
            play_again = input("\nDo you want to play again? (Y/N): ").strip().upper()
            if play_again == "Y":
                break  # restart the outer loop
            elif play_again == "N":
                print("Going back to  toolkit menu...")
                return  # exit the function
            else:
                print("Invalid input. Please enter Y or N.")
