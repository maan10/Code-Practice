import random

def  number(x):
    random_number=random.randint(0,x)
    guess=0
    while guess!= random_number:
        guess=int(input(f"Enter any numbver that is equal and less than {x}:"))
        if  guess>random_number:
            print("Too high")
        elif guess<random_number:
            print("too long try again")
        else:
            print("You have guess the correct number thaat generate by computer {}".format(random_number))