# Lab Assignment 2

# Take prices input
prices = input("Enter prices separated by space: ")
lst = list(map(float, prices.split()))
t = tuple(lst)

# a) Total number of items sold
print("Total number of items sold:", len(t))

# b) Cheapest item
cheapest = min(t)
print("Cheapest item price:", cheapest)

# c) Costliest item
costliest = max(t)
print("Costliest item price:", costliest)

# d) Prices in ascending order
sorted_prices = tuple(sorted(t))
print("Prices in ascending order:", sorted_prices)

# e) Number of costliest items sold
count_costliest = t.count(costliest)
print("Number of costliest items sold:", count_costliest)