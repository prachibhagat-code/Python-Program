#Pattern 1
"""
A
AB
ABC
ABCD
ABCDE
"""
for i in range(1, 6):
    ch = ord('A')
    for j in range(i):
        print(chr(ch), end = "")
        ch += 1
    print()
print("\n")


#Pattern 2
"""
*
* #
* # *
* # * #
* # * # *
"""
for i in range(1, 6):
    for j in range(1, i+1):
        if j % 2 == 1:
            print("*", end = " ")
        else:
            print("#", end = " ")
    print()
print("\n")


#Pattern 3
"""
p
yy
ttt
hhhh
ooooo
nnnnnn
"""
word = "python"

for i in range(len(word)):
    for j in range(i+1):
        print(word[i], end = "")
    print()
print("\n")


#Pattern 4
"""
p
p y
p y t
p y t h
p y t h o
p y t h o n
"""
word = "python"

for i in range(1, len(word)+1):
    for j in range(i):
        print(word[j], end = " ")
    print()
print("\n")