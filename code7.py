"""
Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.
person	Relation
Darth Vader	father
Leia	sister
Han	brother in law
R2D2	droid
"""

def remind(x):
    if x=="Darth Vade":
        return "Luke, I am your father."
    elif x=="Leia":
        return "Luke, I am your sister"
    elif x=="Han":
        return "Luke, I am your brother in law"
    elif x=="R2D2":
        return "Luke, I am your droid"


# print(remind("Darth Vade")
print(remind("Leia"))

eval()
