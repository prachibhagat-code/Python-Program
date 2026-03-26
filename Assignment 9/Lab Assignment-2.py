import matplotlib.pyplot as plt

# Try dataset or manual input
companies = ["Microsoft","Google","Amazon","IBM","Deloitte","Capgemini","ATOS","Amdocs"]
recruitments = []

print("Enter recruitment data:")

for c in companies:
    val = int(input(f"{c}: "))
    recruitments.append(val)

# a) Bar Chart
plt.bar(companies, recruitments)
plt.title("Recruitments by Company")
plt.xticks(rotation=45)
plt.show()

# b) Pie Chart
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()

# c) Customized Pie Chart
plt.pie(recruitments, labels=companies, autopct='%1.1f%%',
        shadow=True, startangle=140)
plt.title("Customized Pie Chart")
plt.show()

# d) Doughnut Chart
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title("Doughnut Chart")
plt.show()

# Compare IBM & Amdocs
ibm = recruitments[companies.index("IBM")]
amdocs = recruitments[companies.index("Amdocs")]

plt.bar(["IBM","Amdocs"], [ibm, amdocs])
plt.title("IBM vs Amdocs Recruitment")
plt.show()