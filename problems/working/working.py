import re
import sys


def main():
    hours = input("Hours: ")
    print(convert(hours))


def convert(hours):
    # first let's check the user inputs the correct format
    # (\d|1[012]) covers 0 to 12, (:[0-5]\d)? is the optional :00 to :59, [AP]M is either AM or PM (uppercase)
    matches = re.search(
        r"^(\d|1[012])(:[0-5]\d)? ([AP]M) to (\d|1[012])(:[0-5]\d)? ([AP]M)$", hours)
    if not matches:
        raise ValueError("This is not the right format")
    else:
        # exceptional cases for midnight and midday, although I am sure there is a more elegant way to do it
        if matches.group(1) == "12" and matches.group(3) == "AM":
            hours_left = 0
        elif matches.group(1) == "12" and matches.group(3) == "PM":
            hours_left = 12
        else:
            # checking through groups if we need to double the value of hours
            hours_left = (int(matches.group(1)) +
                          12) if matches.group(3) == "PM" else int(matches.group(1))

        if matches.group(4) == "12" and matches.group(6) == "AM":
            hours_right = "00"
        elif matches.group(4) == "12" and matches.group(6) == "PM":
            hours_right = "12"
        else:
            hours_right = (int(matches.group(4)) +
                           12) if matches.group(6) == "PM" else int(matches.group(4))

        # checking the minutes and adding them if missing in the input
        mins_left = ":00" if matches.group(2) == None else matches.group(2)
        mins_right = ":00" if matches.group(5) == None else matches.group(5)

        # assembling the newly formatted time to be returned (using n:02 formatting)
        return f"{hours_left:02}{mins_left} to {hours_right:02}{mins_right}"


if __name__ == "__main__":
    main()
