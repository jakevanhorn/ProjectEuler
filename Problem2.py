a = 1
b = 2
b2 = 0
sum = 0

while b < 4000000:
    if b % 2 == 0:
        print(b)
        sum += b
    b2 = b
    b += a
    a = b2
print()
print (sum)