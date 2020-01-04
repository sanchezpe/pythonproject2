# the number of shares of stock purchased/sold (we are assuming this will be the same number)
numberShares=eval(input("Enter number of shares: "))

# price of stock (per share) when purchased
pricePurchase=eval(input("Enter price of stock at purchase: "))

# price of stock (per share) when sold
priceSale=eval(input("Enter price of stock at sale: "))

# amount of money paid for stock (number of shares * price per share when purchased)
amountPaid=numberShares*pricePurchase

# amount of commission paid when purchasing stock
commissionPurchase=amountPaid*4/100

# amount of money received when selling stock (number of shares * price per share when sold)
amountReceived=numberShares*priceSale

# amount of commission paid when selling stock
commissionSale=amountReceived*4/100

# amount “made” by investor (possibly a loss)
# (money received – money paid) – (all commissions paid)
profit=(amountReceived-amountPaid)-(commissionSale+commissionPurchase)

# display the results
print("                        -------------------")
print("Cost of Stock Purchase: $",format(amountPaid, '0.2f'))
print("Commission Purchase:    $",format(commissionPurchase, '0.2f'))
print("Cost of Stock Sale:     $",format(amountReceived, '0.2f'))
print("Commission Sale:        $",format(commissionSale, '0.2f'))
print("                        -------------------")
print("Profit/Loss:            $",format(profit, '0.2f'))