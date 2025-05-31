from random import randint


def main():

    level = get_level()  # to get the level17

    score = 0  # keeps track of the score

    for _ in range(10):  # repeats 10 times, for as many problems to solve
        mistakes = 0  # keeps track of user's mistakes (inside the loop coz 3 tries per problem)
        x = generate_integer(level)
        y = generate_integer(level)
        while mistakes < 3:
            try:
                solution = int(input(f"{x} + {y} = "))
                if solution != (x + y):
                    raise ValueError()
                else:
                    score += 1
                    break
            except ValueError:
                print("EEE")
                mistakes += 1
                if mistakes == 3:  # if user has made 3 mistakes...
                    print(f"{x} + {y} = {x + y}")  # the program prints the answer...

    print(
        f"Score: {score}"
    )  # either after the 10 answers or after the program answers for the 3 mistakes


def get_level():  # prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                raise ValueError()
            return level
        except ValueError:
            pass


def generate_integer(level):  # return the right number according to level (n digits)
    if level == 1:
        return randint(0, 9)
    elif level == 2:
        return randint(10, 99)
    elif level == 3:
        return randint(100, 999)
    else:
        raise ValueError()


if __name__ == "__main__":
    main()
