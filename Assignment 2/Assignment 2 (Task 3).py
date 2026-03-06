#Need to print numbers from 1 to n in one line without spaces, and without using string methods.
#So we will use a loop and print(..., end="").

n = int(input())

for i in range(1, n+1):
    print(i, end = "")