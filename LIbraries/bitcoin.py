import requests
import sys

API_KEY = "f671d6ad6b412c1e7b9f2cafb48851d9e6a4f345cea131f6a1b093b3e22adfd6"

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

# Parse number of Bitcoins
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

# API request with error handling
try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin", 
                          headers={"Authorization": f"Bearer {API_KEY}"})
    response.raise_for_status()
    data = response.json()
    price = float(data["data"]["priceUsd"])
except (requests.RequestException, KeyError, ValueError):
    sys.exit("Error fetching Bitcoin price")

# Calculate and format cost
amount = n * price
print(f"${amount:,.4f}")
