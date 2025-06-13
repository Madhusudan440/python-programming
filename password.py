import random
import string

def generate_password(length):
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    # Define the character sets to use for password generation
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + special_characters

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("-------------------")

    try:
        length = int(input("Enter the desired length of the password: ").strip())
        password = generate_password(length)
        print(f"Generated Password: {password}")

    except ValueError as e:
        print(f"Error: {e}. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
