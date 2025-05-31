import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # initialise a count
    count = 0

    # collecting all the words (plus punctuation) given by splitting s
    words = s.split(" ")
    print(words)

    # trying to catch all the possible char that can come after "um"
    for word in words:
        matches = re.search(r"^um[.,!?;: ]*$", word, re.IGNORECASE)
        if matches:
            count += 1

    return count


if __name__ == "__main__":
    main()
