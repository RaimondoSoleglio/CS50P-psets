# ask the user to input a name in camelCase
camel = input("camelCase: ")


# how do we do this?
snake = ""

# loop through each char of a string until you find Capital letters?

for i in camel:
    # if the character is lowercase we add it to a new string
    if i.islower():
        snake += i
    # otherwise we add _ + the lowercase character
    else:
        snake += ("_" + i.lower())

print(f"snake_case: {snake}")
