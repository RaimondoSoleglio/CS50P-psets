from random import randint

while True:
    try:
        n = int(input("Level: "))  # the user must input a positive integer...
        if n < 1:
            raise ValueError()
        break
    except ValueError:  # ...or they will be prompted again
        pass

solution = randint(1, n)  # Randomly generates an integer between 1 and n


while True:
    try:
        guess = int(input("Guess: "))  # same as above
        if guess < 1:
            raise ValueError()
        if guess < solution:
            print("Too small!")
        elif guess > solution:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
