"""
Transpose a matrix
"""

A = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

print("転置前")
for i in range(len(A)):
    print("{} {} {}".format(A[i][0], A[i][1], A[i][2]))

B = list(map(list, zip(*A)))

print("転置後")
for i in range(len(B)):
    print("{} {} {}".format(B[i][0], B[i][1], B[i][2]))

ofile = open(r'/Users/felix/A.txt', "w+")

for i in range(len(B)):
    ofile.write("{} {} {}".format(B[i][0], B[i][1], B[i][2]) + "\n")

ofile.close()
