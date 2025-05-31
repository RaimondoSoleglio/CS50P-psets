import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # validate through regex
    match = re.search(r"^((\d|[1-9]\d|1\d\d|2[0-4][0-9]|25[0-5])\.){3}(\d|[1-9]\d|1\d\d|2[0-4][0-9]|25[0-5])$", ip)
    # a simplified version of "return True if match else False"
    return match is not None


if __name__ == "__main__":
    main()
