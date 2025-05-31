# defining a function to calculate the formula
def einstein(m):
    e = m * pow(300000000, 2)
    return e


def main():
    # ask for an input from the user, convert it into a number and store it in a var
    m = int(input("What's the mass? "))

    print(einstein(m))


main()
