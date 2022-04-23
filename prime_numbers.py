i = 1
number = 10
numList = [i for i in range(i, number)]

for j in range((i + 1), number):
    numList = list(filter(lambda x: (x % j != 0) or (j == x), numList))

print(numList)
