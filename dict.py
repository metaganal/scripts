"""
Learning the basics of a python dictionary
"""

A = ["a", "d", "c", "b"]
B = ["3", "5", "8", "1"]

d = {}

for i in range(len(A)):
    d[A[i]] = B[i]

print(A)
print(B)
print(d)
