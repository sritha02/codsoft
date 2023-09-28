import random
import string

def generate_password(length):
    # Define character sets for generating the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    
    # Check if the password length is valid
    if length < 8:
        print("Password length should be at least 8 characters.")
        return
    
    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Prompt the user for the desired password length
try:
    password_length = int(input("Enter the desired password length: "))
    
    # Generate and display the password
    generated_password = generate_password(password_length)
    if generated_password:
        print("Generated Password:", generated_password)
except ValueError:
    print("Please enter a valid number for the password length.")
