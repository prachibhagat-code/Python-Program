import pandas as pd

# Creating sample employee data
data = {
    "Employee ID": [101, 102, 103, 104, 105],
    "Employee Name": ["Amit", "Neha", "Raj", "Sneha", "Karan"],
    "Department": ["IT", "HR", "IT", "Finance", "IT"],
    "Designation": ["Developer", "Manager", "Developer", "Analyst", "Developer"],
    "Domain": ["Automotive", "Healthcare", "Automotive", "Banking", "Automotive"]
}

df_emp = pd.DataFrame(data)

# a) Employees in Automotive domain
auto_emp = df_emp[df_emp["Domain"] == "Automotive"]
print("Employees in Automotive domain:")
print(auto_emp)

# b) Details of employee by ID
emp_id = int(input("\nEnter Employee ID: "))
emp_details = df_emp[df_emp["Employee ID"] == emp_id]

print("\nEmployee Details:")
print(emp_details)

# c) List all Developers
developers = df_emp[df_emp["Designation"] == "Developer"]
print("\nList of Developers:")
print(developers)