import pandas as pd

# Try to read CSV, else take input
try:
    df = pd.read_csv("books.csv")
    print("CSV file loaded successfully!\n")
except:
    print("books.csv not found! Enter data manually.\n")
    
    n = int(input("Enter number of books: "))
    data = []

    for i in range(n):
        print(f"\nEnter details for Book {i+1}")
        title = input("Title: ")
        author = input("Author: ")
        edition = input("Edition: ")
        year = int(input("Year: "))
        publisher = input("Publisher: ")
        price = float(input("Price: "))

        data.append([title, author, edition, year, publisher, price])

    df = pd.DataFrame(data, columns=["title","author","edition","year","publisher","price"])


# a) Print complete report
print("\n--- Complete Book List ---")
print(df)

# b) Books of given author
author_name = input("\nEnter author name: ")
print(df[df['author'] == author_name])

# c) Books of given publisher
publisher_name = input("\nEnter publisher name: ")
print(df[df['publisher'] == publisher_name])

# d) Cheapest & Costliest book
print("\n--- Cheapest Book ---")
print(df.loc[df['price'].idxmin()])

print("\n--- Costliest Book ---")
print(df.loc[df['price'].idxmax()])

# e) Sort by year
print("\n--- Sorted by Year ---")
print(df.sort_values(by='year'))