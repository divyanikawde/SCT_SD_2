print("Welcome to the Number Guessing Game!")
print("I have thought of a number between 1 and 100.")
print("Can you guess what it is?")

secret_number = 42 
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low. Try again.")
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print(f" Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        break