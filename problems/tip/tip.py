def main():
    dollars = dollars_to_float(input("How much was the meal? (eg: $50.00): "))
    percent = percent_to_float(input("What percentage would you like to tip? (eg: 15%): "))
    print(dollars, percent)
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # let's strip the dollar sign and, why not, the spaces from leading and trailing - and then convert to float
    return float(d.strip(" $"))


def percent_to_float(p):
    # here we do something similar but with %
    return float(p.strip(" %")) / 100


main()
