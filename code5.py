def curzon(x):
    z= (2**x) +1

    y=(2*x)+1
    if z%y==0:
        print("True")
    else:
        print("fail")

curzon(5)
curzon(10)
curzon(14)