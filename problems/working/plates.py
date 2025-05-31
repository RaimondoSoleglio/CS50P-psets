def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Max 6 char and min 2 char (must be the first condition)
    if minMax(s):
        # Must start with two letters
        if (twoLetters(s) and

            # Numbers must come at the end
            numbersAtEnd(s) and

            # No periods, spaces, or punctuation
            noOtherChars(s)):
            return True
        else:
            return False


# Function for first two letters
def twoLetters(s):
    if s[0].isdigit() or s[1].isdigit():
        return False
    return True


# Function for min and max characters
def minMax(s):
    if len(s) < 2 or len(s) > 6:
        return False
    return True


# Function dealing with numbers
def numbersAtEnd(s):
    i = 0
    zero = True
    digit = False
    while i < len(s):
        if s[i].isalpha() and digit:
            return False
        elif s[i] == "0" and zero:
            return False
        # elif s[i].isdigit() and s[i + 1].isalpha():
            # return False
        elif s[i].isdigit():
            zero = False
            digit = True
        i += 1
    return True


# Function dealing with ascii characters
def noOtherChars(s):
    for i in s:
        if not i.isalnum():
            return False
    return True


main()
