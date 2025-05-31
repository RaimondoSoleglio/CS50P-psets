# user inputs a string

user_str = input("Input: ")
otpt = ""

# maybe we can store all the vowels in a list?
vowels = ["a", "i", "u", "e", "o"]
upper_vowels = [vowel.upper() for vowel in vowels]

# we output a string with no vowels, either lower or uppercase
for char in user_str:
    if not (char in vowels or char in upper_vowels):
        otpt += char

print(f"Output: {otpt}")
