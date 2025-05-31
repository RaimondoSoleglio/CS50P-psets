import requests
import sys
import json

try:
    if len(sys.argv) != 2:
        raise TypeError()
    n = float(sys.argv[1])
except TypeError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
    response.raise_for_status()
    data = response.json()
    value = n * float(data["data"]["priceUsd"])
except requests.RequestException as e:
    print("An error occured: {e}")

print(f"${value:,.4f}")
