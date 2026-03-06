#Largest Number Among Three Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c

print("Largest number is:", largest)