def main():
    userTime = input("What time is it? ")

    # let's use a variable to hold the converted value
    convertedTime = convert(userTime)

    # conditionals
    if 7.0 <= convertedTime <= 8.0:
        print("breakfast time")
    elif 12.0 <= convertedTime <= 13.0:
        print("lunch time")
    elif 18.0 <= convertedTime <= 19.0:
        print("dinner time")
    else:
        return


def convert(time):
    # case of 12-hour time
    if time.endswith("p.m."):
        temp, m = time.rstrip(" .pm").split(":")
        h = float(temp) + 12
        print

    # converting the string into a number formatted as requested by the assignment
    # and considering the case of a.m.
    else:
        h, m = time.rstrip(" .am").split(":")

    # to get minutes into decimals (m * 100 / 60) and then in 100ths
    minConverted = (float(m) * 10 / 6) / 100
    return float(h) + minConverted


if __name__ == "__main__":
    main()
