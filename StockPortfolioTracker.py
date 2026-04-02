# Stock Portfolio Tracker
# Created by Arjun Muluk
# Internship Task 2

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "MSFT": 300,
    "AMZN": 3300
}

portfolio = {}
total_investment = 0

print("📊 Welcome to Stock Portfolio Tracker")

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    
    if stock not in stock_prices:
        print("❌ Stock not available.")
        continue
    
    quantity = int(input("Enter quantity: "))
    
    portfolio[stock] = quantity

# Calculate total investment
print("\n📈 Portfolio Summary:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment
    
    print(f"{stock} - Qty: {quantity}, Price: {price}, Value: {investment}")

print("\n💰 Total Investment:", total_investment)

# Optional: Save to file
save = input("\nDo you want to save this to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            investment = price * quantity
            file.write(f"{stock} - Qty: {quantity}, Value: {investment}\n")
        
        file.write(f"\nTotal Investment: {total_investment}")
    
    print("✅ Data saved to portfolio.txt")


## 📸 Demo
(https://www.linkedin.com/posts/arjun-muluk-6aa938376_codealpha-python-internship-activity-7445365556364558337-lhJF?utm_source=share&utm_medium=member_desktop&rcm=ACoAAF0K-OIBxazuEX0o9OThcK5ZB0EuFP3B-LE)

## 🙌 Learning Outcome
This project helped me understand how to work with real-world data and perform calculations using Python.

---

⭐ Feel free to explore and give feedback!
    
