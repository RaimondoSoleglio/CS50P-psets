from validator_collection import validators, errors, checkers


def main():
    # we store the email after validation
    try:
        email = validators.email(input("What's your email? "), allow_empty=False)
    except errors.EmptyValueError:
        return print("You did not input an email.")
    except errors.InvalidEmailError:
        return print("Invalid")


    # then check after validation
    check = checkers.is_email(email)

    # if checked it's valid
    if check:
        return print("Valid")
    else:
        return print("Invalid")


if __name__ == "__main__":
    main()
