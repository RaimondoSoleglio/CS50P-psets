amount = 50

# condition for the loop to keep going
while amount > 0:
    print(f"Amount Due: {amount}")
    coin = input("Insert Coin: ")

    # different cases of coins
    match coin:
        case "25":
            amount -= 25
        case "10":
            amount -= 10
        case "5":
            amount -= 5

print(f"Change Owed: {abs(amount)}")
