import sys


def main():
    # checks the number and type of arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many coomand-line arguments")
    elif not (sys.argv[1]).endswith(".py"):
        sys.exit("Not a Python file")

    # initialises a variable for the Lines Of Code count
    loc = 0

    try:
        with open(sys.argv[1], "r") as file:

            # we read all the lines of the file and make a list of them
            read_file = file.readlines()

            # loops through the elements of the list
            for line in read_file:
                if line.lstrip(" ").startswith("#") or line.lstrip(" ") == "\n":
                    continue
                else:
                    # we add to the LOC only the lines that aren't empty or comments
                    loc += 1

    except FileNotFoundError():
        # checks for file existence
        sys.exit("File does not exist")

    print(loc)


if __name__ == "__main__":
    main()
