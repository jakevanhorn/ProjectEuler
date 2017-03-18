numPrimeT = False
countNum = 3
countPrime = 1

while(numPrimeT == False):
    print(countNum)
    for a in range(2, countNum):
        if countNum % a == 0:
            break
        if a == countNum - 1:
            countPrime += 1
            print("Prime")
    if countPrime == 10001:
        numPrimeT = True
        break
    else:
        countNum += 1

print(countNum)
