# let's write a function called convert() that will convert emoticon into emoji
def convert(str):
    newStr = str.replace(":)", "🙂").replace(":(", "🙁")
    # after the replacement we return the value string
    return newStr


def main():
    # in the main() function first I ask for an input...
    wys = input("Feel free to describe how you feel with emoticons...: ")

    # ...and then we print the returned value of the function convert()
    print(convert(wys))


main()
