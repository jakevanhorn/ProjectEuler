import random

listRolls = []
rollAmount = []

win = 0
total = 0

for t in range (0,100000):
    list.clear(listRolls)
    list.clear(rollAmount)

    for a in range (0,5): #Make five dice rolls and sort them
        randNum = random.randint(1,6)
        listRolls.append(randNum)
    list.sort(listRolls)

    for a in range (0,6): #Make list of number of each dice roll
        numberCount = listRolls.count(a + 1)
        rollAmount.append(numberCount)
    largeAmount = rollAmount[0]
    largeNum = 1

    for a in range (1,6): #Find number with most rolls
        if rollAmount[a] > largeAmount:
            largeAmount = rollAmount[a]
            largeNum = a + 1
    remain = 5 - largeAmount

    for a in range (0,2):
        if remain == 0:
            break
        for b in range (0, remain):
            randNum = random.randint(1,6)
            if randNum == largeNum:
                remain -= 1

    if remain <= 0:
        win += 1
        total += 1
    else:
        total += 1

print(win)
print(total)
print(win/total)