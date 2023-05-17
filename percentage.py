def per(price,discount):
   return round(price - (price * discount)/100, 2)
# a=per(1500,50)
a=per(100,75)

print("The discount is ",a)