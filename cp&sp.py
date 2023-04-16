def sellingprice(cost_price,no_of_items,profit):
    sp = cost_price * (1+profit/100)
    tsp = sp * no_of_items
    return tsp / no_of_items
    
cost_price = int(input())
no_of_items = int(input())
profit = int(input())

selling = sellingprice(cost_price,no_of_items,profit)
print(selling)


#cp/sp