"""
Create a new dict via a function
"""


def create_dict(a, b):
    newdict = {}
    for i in range(len(a)):
        newdict[a[i]] = b[i]

    return newdict


A = ["a", "b", "c"]
B = ["1", "2", "3"]

mydict = create_dict(A, B)

print(A)
print(B)
print(mydict)
