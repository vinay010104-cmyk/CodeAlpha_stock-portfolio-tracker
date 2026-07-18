stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 170
}

total = 0

while True:
    stock = input("Enter stock name (or type exit): ").upper()

    if stock == "EXIT":
        break

    if stock in stocks:
        quantity = int(input("Enter quantity: "))
        value = stocks[stock] * quantity
        total += value

        print("Investment for", stock, "=", value)
    else:
        print("Stock not found")

print("Total Investment =", total)

# Save result in file
file = open("portfolio.txt", "w")
file.write("Total Investment = " + str(total))
file.close()

print("Result saved in portfolio.txt")
