import sys

list = {}

while True:
    try:
        item = input().upper().strip()  # case insensitive
        if item in list.keys():   # adding to the value if key exists...
            list[item] += 1
        else:   # adding key if it does not exist
            list[item] = 1
    except EOFError:
        sorted_list = {key: list[key] for key in sorted(list)}  # sorting the dict keys
        for sorted_item in sorted_list:
            print(f"{list[sorted_item]} {sorted_item}")
        sys.exit(0)
