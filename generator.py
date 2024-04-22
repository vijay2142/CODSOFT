import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Length must be a positive integer")
            return
        password = generate_password(length)
        print("Generated Password:", password)

    except ValueError:
        print("Error:", ve)
        print("Please enter a valid positive integer for password length.")

if __name__ == "__main__":
    main()
