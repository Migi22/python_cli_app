

def run():
    print("\nLaunching Currency converter...")

    # Welcome message and menu for the currency converter.
    print("""
          \nWelcome to the currency converter feature of the toolkit.
          
          Currency Converter Menu:
          1. Exchange
          2. Back to Menu
          """)
    
    # Looping for the choice of the user until it breaks the loop
    while True:
        choose = input("Please select 1 or 2 to proceed: ").strip() # Prompt user for menu choice
        
        if choose == "1":
            print("You selected currency exchange") #TODO: Remove this after the function is done. This is a placeholder
            #currency_exchange()
        elif choose == "2":
            print("Going back to the menu")
            break
        else:
            print("Invalid choice. Please try again.")

    
