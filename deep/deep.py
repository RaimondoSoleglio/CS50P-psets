def main():
    answer = input(
            "What is the Answer to the Great Question of Life, the Universe and Everything? ").strip().lower()
    solution(answer)


def solution(x):
    if (x == "42") or (x == "forty-two") or (x == "forty two"):
        print("Yes")
    else:
        print("No")


main()
