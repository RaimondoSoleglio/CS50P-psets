import inflect
import sys

from datetime import date, timedelta, datetime


def main():
    # take user input
    user_input = input("Your birthday? ")

    # check ISO 8601 format otherwise exit cause of ValueError
    try:
        datetime.strptime(user_input, "%Y-%m-%d")
    except ValueError:
        sys.exit("Input the date in ISO 8601 format, please")

    # create two date() objects for today and inputted date
    bday = date.fromisoformat(user_input)
    today = date.today()

    # timedelta: the difference between today and bday
    td = today - bday

    # converts timedelta into minutes
    minutes = td_to_minutes(td)

    # converts minutes into literals
    output = minutes_to_literals(minutes)

    print(f"{output.capitalize()} minutes")


def td_to_minutes(td):
    seconds = round(td.total_seconds())
    minutes = round(seconds / 60)
    return minutes


def minutes_to_literals(minutes):
    # initialise inflect
    p = inflect.engine()
    # proper formatting
    min_literal = (p.number_to_words(minutes)).replace("and ", "")
    return min_literal


if __name__ == "__main__":
    main()
