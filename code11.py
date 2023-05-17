def card_pin(x):
    return "*"*len(x[:-4]) +x[-4:]


p=card_pin("123232452134212")
print(p)