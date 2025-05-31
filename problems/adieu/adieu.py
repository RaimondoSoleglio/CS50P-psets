import inflect  # I got this hint from CS50

p = inflect.engine()

adieu = "Adieu, adieu, to "
list = []  # this list will be populated by the names as they are inputted...

while True:
    try:
        name = input("Name: ")
        list.append(name)  # ...here
    except EOFError:
        str = p.join(list)  # this will create a string according to the rules requested
        print(adieu + str)
        break
