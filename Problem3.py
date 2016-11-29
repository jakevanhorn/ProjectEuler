import math

number1 = 600851475143
prime = False

for a in range (int(math.sqrt(number1)), 1, -1):
    if number1 % a == 0:
        for b in range (a-1, 0, -1):
            if b == 1:
                prime = True
                break
            if a % b == 0:
                break
    if prime == True:
        print(a)
        break

