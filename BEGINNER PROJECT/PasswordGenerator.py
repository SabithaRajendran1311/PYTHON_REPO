import random
import string

def generate_password(length):
    if length < 4:
        return "Password too short!"

    # Define character sets
    letters = string.ascii_letters  # A-Z, a-z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # Special characters

    # Ensure password includes at least one letter, one digit, and one symbol
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest with random characters
    all_chars = letters + digits + symbols
    password += random.choices(all_chars, k=length - 3)

    # Shuffle the list to avoid predictable order
    random.shuffle(password)

    return ''.join(password)

# Ask user for password length
length = int(input("Enter desired password length: "))
print("Generated password:", generate_password(length))
