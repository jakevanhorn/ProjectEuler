import math

num = 0
testT = False

while (testT == False):
    num += 20
    for a in range (11,22):
        if a == 21:
            testT = True
            break
        if num % a != 0:
            break

print(num)