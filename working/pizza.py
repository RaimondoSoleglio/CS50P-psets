from tabulate import tabulate
import sys
import csv


def main():
    # check for the right number of args
    if not len(sys.argv) == 2 or not (sys.argv[1]).endswith(".csv"):
        sys.exit("Wrong number of args or filetype")
    else:
        try:
            with open(sys.argv[1], "r") as f:
                # read all lines into a reader
                reader = csv.reader(f)
                # using tabulate instructions to edit the tab properly
                print(tabulate(reader, headers="firstrow", tablefmt="grid"))
        # don't forget to omit () when using except
        except FileNotFoundError:
            sys.exit("File does not exist")


if __name__ == "__main__":
    main()
