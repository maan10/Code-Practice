'''
y=range(10)
for x in  y:
    print(x)
'''
    

"""
for i in range(-10,-1):
    # if i==7:
    #     # continue
    #     break
    print(i)
"""
number=int(input("Enter number of row"))
for i in range(1,number+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
else:
    print("Lol")

logo="Hi work hard"
n=len(logo)

for i in range(n) :
    print(i, "=" ,logo[i ]) 