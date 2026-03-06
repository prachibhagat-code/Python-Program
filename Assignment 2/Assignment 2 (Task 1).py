#Pattern 1
"""
1
12
123
1234
12345
"""
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end = "")
    print()
print("\n")


#Pattern 2
"""
1
22
333
4444
55555
"""
for i in range(1, 6):
    for j in range(i):
        print(i, end = "")
    print()
print("\n")


#Pattern 3
"""
1
21
321
4321
54321
"""
for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end = "")
    print()
print("\n")


#Pattern 4
"""
1
1 0
1 0 1
1 0 1 0
1 0 1 0 1
"""
for i in range(1, 6):
    for j in range(1, i+1):
        print(j % 2, end = " ")
    print()
print("\n")


#Pattern 5
"""
2
4 6
8 10 12
14 16 18 20
"""
num = 2
for i in range(1, 5):
    for j in range(i):
        print(num, end = " ")
        num += 2
    print()
print("\n")


#Pattern 6
"""
*
**
***
****
*****
"""
for i in range(1, 6):
    for j in range(i):
        print("*", end = "")
    print()
print("\n")