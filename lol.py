import math

'''
def radian(x):
    x=x * 180/math.pi
    x=round(x,1)
    print(x)
'''
def radians_to_degrees(rad):
	return round(math.radians(rad),1)


print(radians_to_degrees(1145.9))