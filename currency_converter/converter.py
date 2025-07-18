'''handles fetching of exchange rates'''

from dotenv import load_dotenv
import os
import requests
import emoji_util

load_dotenv() # load variable from .env
api_key = os.getenv("EXCHANGE_API_KEY")

def currency_exchange():
    while True:
        print("\n=== Exchange on process ===")
        base_currency = input("Please enter the base currency: ").upper()
        target_currency = input("Please enter the target currency: ").upper()

        try:
            amount = float(input("Please enter the amount to convert: "))
        except ValueError:
            print("Invalud amount. Please enter a valid number")
            continue
        
        #API Calling
        api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"

        try:
            response = requests.get(api_url)
            data = response.json()

            # Check for any error in API response
            if data["result"] != "success":
                print(f"Error: {data.get('error-type', 'Unkown error')}")
                continue
            
            rates = data["conversion_rates"]

            if target_currency not in rates:
                print(f"{emoji_util.CROSS} Unsupported currency: {target_currency}")
                continue

            # Display message for the result
            converted_amount = amount * rates[target_currency]
            print(f"\nConversion complete {emoji_util.CHECK} {amount: .2f} {base_currency} = {converted_amount: .2f} {target_currency}")

        except requests.RequestException as e:
            print(f"{emoji_util.CROSS} Network error:", e)
            continue
        except:
            print("An error occured.")

        # Prompt user to convert another or not
        is_convert_another = input("Convert another? Y/N ").strip().upper()
        if is_convert_another != "Y":
            break

   