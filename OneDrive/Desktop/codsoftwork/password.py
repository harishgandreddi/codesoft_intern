
import random
import string

def password_generator():
    print("Password Generator")
    print("------------------")

    # Prompt the user to specify the desired length of the password
    while True:
        try:
            length = int(input("Enter the length of the password (min 8): "))
            if length < 8:
                print("Password length should be at least 8 characters.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Ask the user to specify the complexity of the password
    while True:
        print("Choose the complexity of the password:")
        print("1. Simple (only letters)")
        print("2. Medium (letters and numbers)")
        print("3. Complex (letters, numbers, and special characters)")
        choice = input("Enter your choice (1/2/3): ")
        if choice in ['1', '2', '3']:
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    # Generate the password based on the user's choice
    if choice == '1':
        characters = string.ascii_letters
    elif choice == '2':
        characters = string.ascii_letters + string.digits
    elif choice == '3':
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    # Display the generated password
    print("Generated Password : ", password)

def main():
    password_generator()
    while True:
        again = input("Do you want to generate another password? (yes/no): ")
        if again.lower() == "yes":
            password_generator()
        elif again.lower() == "no":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()


