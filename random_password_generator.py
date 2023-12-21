"""
# Ask the user if the want to generate a password or not
# If yes, ask for password length
# generate the password
# Print password
# If initial password is no exit the program
"""
import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_lentth = int(input("How long do you want your password"))

    random.shuffle(characters)

    password = []

    for x in range(password_lentth):
        password.append(random.choice(characters))
    random.shuffle(password)

    password = "".join(password)
    print(password)

option = input("Do you want to generate a password? (Y/N)")
option = option.lower()

while True:
    if option == "y":
        generate_password()
        quit()
    elif option == "n":
        print("Program ended")
        quit()
    else: 
        print("Invalid input")
        option = input("Please input (Y/N): ")
