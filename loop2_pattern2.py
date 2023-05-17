"""

n=int(input("enter number od row "))
m=int(input("enter number of coloumn"))

for i in range(n+1):
    for j in range(m+1):
        print("x",end=" ")
    print() 

"""


"""
Pattern 2


row=int(input("enter number of row"))
for i in range(0,row+1):
    for j in range(0,i+1):
        print("*",end=" ")
    print()
"""

n=int(input("Enter number of row"))

for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print(" ")