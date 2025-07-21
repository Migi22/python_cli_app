import random
import string

def generate_password(length=12):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_chars = letters + digits + symbols

    # has at least one of each
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    password += random.choices(all_chars, k=length - 3)
    random.shuffle(password)

    return ''.join(password)

def custom_password_generator():
    try:
        length = int(input("Enter desired password length: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    char_pool = ""

    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        print("You must select at least one character type!")
        return

    password = ''.join(random.choices(char_pool, k=length))
    print("Your generated password is:", password)
  
