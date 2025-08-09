# Hardcoded dictionary of stock prices
stock_prices = {"AAPL": 180, "TSLA": 250, "GOOG": 2700}

# Input stock name and quantity
stock_name = input("Enter stock name (e.g., AAPL): ").upper()
quantity = int(input("Enter quantity: "))

# Calculate total investment
if stock_name in stock_prices:
    total = stock_prices[stock_name] * quantity
    print(f"Total investment in {stock_name}: ${total}")
else:
    print("Stock not found.")
