def main():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
        except ValueError:
            continue
        try:
            if int(x) > int(y):    # we eliminate the case where y is greater than x
                raise ValueError()
            # returning the value we also break out of the while loop
            return print(conversion(int(x), int(y)))
        except ValueError:  # we handle the case of a non-digit input
            pass
        except ZeroDivisionError:  # we handle the case of y == 0
            pass


def conversion(x, y):
    percentage = int(round(x / y * 100))
    if percentage <= 1:   # the case of <= 1%
        return "E"
    elif percentage >= 99:   # the case of >= 100%
        return "F"
    else:
        return f"{percentage}%"


main()
