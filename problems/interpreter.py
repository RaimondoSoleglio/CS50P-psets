def main():
    expression = input("Expression: ")

    # split the string into 3 variables, using a space as a separator
    x, y, z = expression.split(" ")

    # initiating a variable
    solution = 0

    # 0 case
    if y == "/" and z == "0":
        return

    # 4 different cases
    match y:
        case "+":
            solution = float(x) + float(z)
        case "-":
            solution = float(x) - float(z)
        case "*":
            solution = float(x) * float(z)
        case "/":
            solution = float(x) / float(z)

    # printing with 1 decimal point formatting
    print(f"{solution:.1f}")


main()
