class Solution(object):
    def __init__(self, k, fibArr, numsArr):
        self.k = k
        self.fibArr = fibArr
        self.numsArr = numsArr

    def sum_finder(self):
        i = 0
        sum1 = 0
        fibA = self.fibArr

        while i < len(fibA):
            if fibA[i] < 0:
                if sum1 == k:
                    return self.numsArr
                self.numsArr[i] = fibA[i]
                sum1 = fibA[i] + sum1
            i = i + 1

    def fib_finder(self):
        return self.sum_finder(self.fibArr)
k = 19
fibArr = [-1 for i in range(k)]
numsArr = [-1 for i in range(k)]

def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)
m = 0
index = 0
while fib(m - 1) <= k:
    fibArr[index] = fib(m)

print(Solution(k, fibArr, numsArr))
