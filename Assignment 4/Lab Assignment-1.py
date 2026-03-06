# Lab Assignment 1

# Take input from user
numbers = input("Enter integers separated by space: ")
lst = list(map(int, numbers.split()))
t = tuple(lst)

# a) Total number of items
print("Total number of items:", len(t))

# b) Last item
print("Last item:", t[-1])

# c) Reverse order
print("Tuple in reverse order:", t[::-1])

# d) Check if 5 is present
if 5 in t:
    print("Yes")
else:
    print("No")

# e) Remove first and last, sort remaining
if len(t) > 2:
    new_tuple = t[1:-1]
    sorted_tuple = tuple(sorted(new_tuple))
    print("After removing first & last and sorting:", sorted_tuple)
else:
    print("Not enough elements to remove first and last.")