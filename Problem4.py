number1 = 1
size = 0
pala = False
return1 = 0
list1 = []
list2 = []

for a in range (100,1000):
    for b in range (100,1000):
        number1 = a*b
        list2.append(number1)

list.sort(list2)
list.reverse(list2)

for a in range (len(list2) - 1, -1, -1):
    number1 = str(list2[a])
    list.clear(list1)
    list1 = list(number1)
    size = len(list1)
    if size == 5:
        if list1[0] == list1[4] and list1[1] == list[3]:
            pala = True
            return1 = "".join(list1)
    if size == 6:
        if list1[0] == list1 [5] and list1[1] == list1 [4] and list1[2] == list1 [3]:
            pala = True
            return1 = "".join(list1)
    if pala == True:
        break     

print(return1)


