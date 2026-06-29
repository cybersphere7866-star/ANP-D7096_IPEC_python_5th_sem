secret = 37

while True:
    guess = int(input("Enter Guess: "))

    if guess == secret:
        print("Correct Guess")
        break
    elif guess > secret:
        print("Too High")
    else:
        print("Too Low")