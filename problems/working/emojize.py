import emoji  # import this library from the amazing Kim

str = input("Input: ")  # ask for input

print(emoji.emojize(f"Output: {str}", language="alias"))  # apply with aliases
