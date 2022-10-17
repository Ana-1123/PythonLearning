# Cerinta: Write a function that receives a list of numbers and
#         returns a list of the prime numbers found in it.

def isPrime(nr):
    if nr <= 1:
        return False
    for i in range(2, int(nr / 2) + 1):
        if nr % i == 0:
            return False
    return True


def getPrimeNumbers(numberList):
    primeNrList = []
    for i in numberList:
        if isPrime(i):
            primeNrList.append(i)
    return primeNrList

# def getPrimeNumbers(numberList):
#     f = []
#     primeNrList = filter(isPrime, numberList)
#     for i in primeNrList:
#         f.append(i)
#     return f


if __name__ == '__main__':
    print(getPrimeNumbers([3, 45, 1, 0, 6, 7, 13, 12]))
