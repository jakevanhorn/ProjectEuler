import math

numPrimeT = False
countNum = 2
countPrime = 0

while(numPrimeT == False):
    for a in range (2, countNum - 1):
        if countNum % a == 0:
            break
        if a == countNum - 1:
            countPrime += 1
            print(countNum)
    if countPrime == 10001:
        break
    else:
        countNum += 1

print(countNum)
