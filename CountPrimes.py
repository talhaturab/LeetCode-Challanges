from cmath import sqrt
from itertools import count


n = 5000000

PrimeNumber = [True] * n
PrimeNumber[0] = PrimeNumber[1] = False
limit = round(sqrt(n).real)
for number in range(2, limit+1):
    if PrimeNumber[number]:
        for i in range(number*number, n, number):
            PrimeNumber[i] = False

print(sum(PrimeNumber))