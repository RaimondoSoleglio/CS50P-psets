import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # pattern to catch http, https, www and extract the video code
    matches = re.search(
        # .+ for all that comes before src, same concept at the end after the video code
        # s? to make the s optional, same for the group www.
        # (?P<code>) to catch the group
        r".+src=\"https?://(?:www.)?youtube\.com/embed/(?P<code>\w+)\".+", s, flags=re.IGNORECASE)
    if matches:
        # reformat into the new address using groups
        return f"https://youtu.be/{matches.group("code")}"
    else:
        return None


if __name__ == "__main__":
    main()
