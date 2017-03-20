"""
    George Fox University 2017 High School Programming Contest
    Wilson High School
    Division II - Team 0x0C
    Problem 7
    Language: Python 3.4
"""

def checkletter(let):
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(0,26):
        if let == alpha[i]:
            return i

def compareLet(let1,let2):
    num1 = checkletter(let1)
    num2 = checkletter(let2)
    if num1 < num2: return 1
    elif num2 < num1: return 2
    else: return 0

def compareWord(word1,word2):
    for i in range(len(word1)):
        if compareLet(word1[i],word2[i]) == 1: return 1
        elif compareLet(word1[i],word2[i]) == 2: return 2
    return 0

num_sets = input()
datasetinput = []
datasets = []
numerical = []
alpha = []

for i in range(int(num_sets)):
    datasetinput.append(input())

datasets = datasetinput

for a in range(int(num_sets)):
    bigNum = 10000
    for i in range(len(datasets)):
        holder = datasets[i].split()
        spot = int(holder[len(holder)-1])
        if (spot < bigNum):
            bigNum = spot
            place = i
    numerical.append(datasets[place])
    datasets.pop(place)

for i in datasets:
    print(i)

datasets = datasetinput

print()

for i in datasets:
    print(i)

for a in range(len(datasetinput)):
    place = 0
    lowWord = "zzz"
    for i in range(len(datasets)):
        if compareWord(lowWord,datasets[i]) == 2:
            lowWord = datasets[i]
            place = i
    alpha.append(datasets[place])
    datasets.pop(place)

# print()
# for i in numerical:
#     print(i)

# print()
# for i in alpha:
#     print(i)