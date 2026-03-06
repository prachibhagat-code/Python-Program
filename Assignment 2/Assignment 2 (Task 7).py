#Prime Number Finder Program

# Input and validation using while loop
while True:
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))

    if start > 0 and end > start:
        break
    else:
        print("Invalid input! Start must be > 0 and end must be greater than start.")

print("\nPrime numbers between", start, "and", end, "are:")

# Checking prime numbers using for loop
for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end = " ")
