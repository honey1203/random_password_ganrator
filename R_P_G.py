import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    """Generate a random password based on specified criteria."""
    character_set = ""
    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation
    
    if not character_set:
        raise ValueError("At least one character type must be selected.")
    
    return ''.join(random.choice(character_set) for _ in range(length))

def get_valid_input(prompt, valid_options):
    """Prompt the user for input and validate it against valid options."""
    while True:
        value = input(prompt).lower()
        if value in valid_options:
            return value
        print(f"Invalid input. Please enter one of the following: {', '.join(valid_options)}")

def main():
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter the desired password length (e.g., 12): "))
        if length < 1:
            raise ValueError
        
        use_letters = get_valid_input("Include letters? (yes/no): ", ["yes", "no"]) == "yes"
        use_numbers = get_valid_input("Include numbers? (yes/no): ", ["yes", "no"]) == "yes"
        use_symbols = get_valid_input("Include symbols? (yes/no): ", ["yes", "no"]) == "yes"
        
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"\nGenerated password: {password}")
    
    except ValueError:
        print("Invalid input. Please enter a valid number for length.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
