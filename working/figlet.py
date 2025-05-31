from pyfiglet import Figlet
import sys

# for reference
# figlet = Figlet()
# figlet.getFonts()
# figlet.setFont(font=f)
# print(figlet.renderText(s))

figlet = Figlet()

if len(sys.argv) == 1:
    figlet.setFont(font="standard")
    str = input("Input: ")
    print(figlet.renderText(str))
elif len(sys.argv) == 3:
    try:
        sys.argv[2] in figlet.getFonts()
    except:
        sys.exit("Invalid usage")
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        figlet.setFont(font=sys.argv[2])
        str = input("Input: ")
        print(figlet.renderText(str))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")


