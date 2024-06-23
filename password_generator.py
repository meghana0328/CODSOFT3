import random
import string

def generate_password(length):
    if length < 1:
        return "Password length should be at least 1"

    # Characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        # Prompt the user for the password length
        length = int(input("Enter the desired length of the password: "))
        
        # Generate the password
        password = generate_password(length)
        
        # Display the password
        print("Generated Password:", password)
    
    except ValueError:
        print("Please enter a valid number for the length.")

if __name__ == "__main__":
    main()
