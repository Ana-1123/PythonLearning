def cmmdc(a, b):
    if b == 0:
        return a
    else:
        return cmmdc(b, a % b)


k = 0


def cmmdc_multiple():
    global k
    k = int(input('Introduceti cate numere:'))
    numere = []

    for i in range(1, k + 1):
        n = int(input('Introdu un numar'))
        numere.append(n)

    n1 = numere[0]
    numere.pop(0)

    for i in numere:
        n2 = i
        c = cmmdc(n1, n2)
        n1 = c

    print(c)


if __name__ == '__main__':
    cmmdc_multiple()
