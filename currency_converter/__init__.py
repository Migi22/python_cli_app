from .converter import currency_exchange

def run():
    print("\n\nLaunching Currency converter...")

    # Welcome message
    print("\nWelcome to the currency converter feature of the toolkit.")
    
    # Looping for the choice of the user until it breaks the loop
    while True:
        # Menu for the currency converter
        print("""
              Currency Converter Menu:
              1. Exchange
              2. Back to Menu""")
        
        choose = input("\nPlease select 1 or 2 to proceed: ").strip() # Prompt user for menu choice
        
        if choose == "1":
            currency_exchange()
        elif choose == "2":
            print("Going back to the menu")
            break
        else:
            print("Invalid choice. Please try again.")

    
