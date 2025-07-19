
def run():
    print("\n\nLaunching Mini Quiz Game module...")

    # Welcome message
    print("""
    \nWelcome to the mini quiz game of the toolkit. Have fun ;)
    """)

    # While loop for selecting the menu, will stop when choosing the 3 and go back to the main menu of the toolkit
    while True:
        # Menu for the Mini Game
        print("""
              Mini Quiz Game Menu:
              1. Start
              2. Highscores 
              3. Back to Menu""")
        
        # Prompt user for menu choice
        choice = input("\nPlease select 1, 2, or 3 to proceed: ").strip() 
        
        # Menu choices
        if choice == "1":
            start_quiz()
        elif choice == "2":
            quiz_highscores()
        elif choice == "3":
            print("Going back to the main menu...")
            break
        else:
            print("Invalid input. Please enter only choices 1, 2, and 3 only.")
