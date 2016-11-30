import math

result1 = 0
result2 = 0
result3 = 0

for a in range (1,101):
    result1 += a

result1 = result1 ** 2

for a in range (1,101):
    result2 += a ** 2

result3 = result1 - result2

print(result1)
print(result2)
print(result3)