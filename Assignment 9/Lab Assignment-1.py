import pandas as pd
import matplotlib.pyplot as plt

# Try reading CSV
try:
    df = pd.read_csv("sales.csv")
    print("CSV Loaded Successfully")
except:
    print("sales.csv not found! Enter data manually")
    
    months = []
    total_profit = []
    
    for i in range(12):
        m = input(f"Enter month {i+1}: ")
        p = int(input("Enter profit: "))
        months.append(m)
        total_profit.append(p)

    df = pd.DataFrame({
        "month": months,
        "total_profit": total_profit
    })

# a) Line Plot
plt.plot(df['month'], df['total_profit'], marker='o')
plt.title("Total Profit per Month")
plt.show()

# b) Multiline Plot (Assuming columns exist or ask)
products = ["facecream","facewash","toothpaste","bathingsoap","shampoo","moisturizer"]

for p in products:
    if p not in df.columns:
        df[p] = [int(input(f"Enter {p} sale for each month: ")) for _ in range(len(df))]

for p in products:
    plt.plot(df['month'], df[p], label=p)

plt.legend()
plt.title("Product Sales")
plt.show()

# c) Bar Chart (Facecream & Facewash)
plt.bar(df['month'], df['facecream'], label="Facecream")
plt.bar(df['month'], df['facewash'], label="Facewash")
plt.legend()
plt.title("Facecream vs Facewash")
plt.show()

# d) Pie Chart (Total yearly sales)
total_sales = [df[p].sum() for p in products]

plt.pie(total_sales, labels=products, autopct='%1.1f%%')
plt.title("Yearly Product Sales")
plt.show()