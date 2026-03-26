import pandas as pd

# Take input from user
n = 5
data = []

print("Enter details for 5 states:\n")

for i in range(n):
    print(f"\nState {i+1}")
    name = input("State Name: ")
    area = float(input("Area (in sq km): "))
    population = int(input("Population: "))

    data.append([name, area, population])

df = pd.DataFrame(data, columns=["State", "Area", "Population"])

# Add Population Density column
df["Density"] = df["Population"] / df["Area"]

# a) Complete information
print("\n--- State Data ---")
print(df)

# b) Largest Area
print("\nState with Largest Area:")
print(df.loc[df['Area'].idxmax()]["State"])

# c) Largest Population
print("\nState with Largest Population:")
print(df.loc[df['Population'].idxmax()]["State"])

# d) Population Density already calculated

# e) Highest Population Density
print("\nState with Highest Population Density:")
print(df.loc[df['Density'].idxmax()]["State"])