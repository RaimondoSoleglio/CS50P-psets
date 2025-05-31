import sys

def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0

    while True:
        try:
            user_input = input("Item: ").title()   # capitalises the first letter only
            total += menu[user_input]
            print(f"Total: ${total:.2f}")   # formatting output with two digits
        except KeyError:  # handles the case an item is not on the menu
            pass
        except EOFError:
            sys.exit(0)


main()
