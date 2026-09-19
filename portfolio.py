# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 175,
    "MSFT": 420
}

portfolio = {}
total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available. Please choose from the available stocks.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    except ValueError:
        print("Please enter a valid quantity.")

print("\n===== PORTFOLIO SUMMARY =====")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_investment += value
    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}")

print("--------------------------------")
print(f"Total Investment: ${total_investment}")
print("Thank you for using the Stock Portfolio Tracker!")
