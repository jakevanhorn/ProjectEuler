sum = 0

for a in range(1,1000):
    if a % 3 == 0:
        sum += a
    elif a % 5 == 0:
        sum += a
print(sum)