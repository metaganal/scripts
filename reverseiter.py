"""
Print 1 to 100 in reverse decrementing by 2
"""

for i in reversed(range(0, 101, 2)):
    if i == 0:
        print(1)
    else:
        print(i)
