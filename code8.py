'''Create a function that takes two numbers and a mathematical operator + - / * and will perform a calculation with the given numbers.
'''

def operator(x,y,z):
    if y=="/" and z==0:
        print("Can't divide by 0!")
    elif y=="+":
        print(x+z)
    elif y=="-":
        print(x-z)
    elif y=="*":
        print(x*z)
    elif y=="/":
        print(x/z)
    
# operator(4,"/",2)

operator(4,"/",0)


'''
1
def calculator(n1, operator, n2):
	try: 
		return eval(str(n1)+operator+str(n2))
	except ZeroDivisionError:
		return "Can't divide by 0!"
'''

'''
def calculator(num1, operator, num2):
  if operator == '/' and num2 == 0:
    return "Can't divide by 0!"
  return eval('num1' + operator + 'num2')
'''