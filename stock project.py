stock_prices={"AAPL":180,"TSLA":250,"GOOG":140}
total_investment=0
while True:
    name=input("Enter the name of stock:")
    if name.lower()=='done':
        break
    if name in stock_prices:
        quantity=int(input('Enter the quantity:'))
        cost=stock_prices[name]*quantity
        total_investment+=cost
        print(f"Added {quantity} shares of {name}=${cost}")
    else:
        print("Stock not found,try again")
print(f"Total Investment:${total_investment}")



