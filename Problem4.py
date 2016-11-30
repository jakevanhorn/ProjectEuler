listFull = []
listNum = []
product = 0
testNum = 0
size = 0
pala = False
result = 0

for a in range (100,1000):
    for b in range (100,1000):
        product = a*b
        listFull.append(product)

list.sort(listFull)
list.reverse(listFull)

for a in range (0, len(listFull)):
    testNum = str(listFull[a])
    list.clear(listNum)
    listNum = list(testNum)
    size = len(listNum)
    if size == 5:
        if listNum[0] == listNum[4] and listNum[1] == listNum[3]:
            pala = True
            result = "".join(listNum)
    if size == 6:
        if listNum[0] == listNum[5] and listNum[1] == listNum[4] and listNum[2] == listNum[3]:
            pala = True
            result = "".join(listNum)
    if pala == True:
        break     

print(result)


