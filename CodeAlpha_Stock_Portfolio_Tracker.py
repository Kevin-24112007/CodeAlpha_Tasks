import csv

stock_price_data = {"ALPHA": 142.50, "BETA" : 88.25, "GAMMA" : 204.10, "THETA" : 54.10, "ECHO" : 150.55}
invested_amount = 0

print("----------STOCK PORTFOLIO TRACKER----------\n")

number_of_stocks = int(input("Enter the number of stocks: "))

with open("investment.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Stock", "Price", "Quantity", "Investment"])

    for i in range(number_of_stocks):
        stock_name = input("\nEnter the stock name: ").upper()
        if stock_name not in stock_price_data:
            print(f"Stock {stock_name} not found")
            continue

        stock_qty = int(input("Enter the stock quantity: "))
        stock_amount_invested = stock_price_data[stock_name] * stock_qty
        invested_amount += stock_amount_invested

        print(f"Investment in {stock_name} = {stock_amount_invested}")

        writer.writerow([stock_name,stock_price_data[stock_name],stock_qty,stock_amount_invested])

    writer.writerow([])
    writer.writerow(["Total Investment", invested_amount])

print(f"\nTotal investment = {invested_amount}")
print("Investment data saved to investment.csv")