
def palindromtuple(nrlist):
    nrpalindrom = 0
    for nr in nrlist:
        if palindrom(nr):
            if nrpalindrom == 0:
                maxpalindrom = nr
            if nr > maxpalindrom:
                maxpalindrom = nr
            nrpalindrom = nrpalindrom + 1
    return (nrpalindrom, maxpalindrom)


def palindrom(nr):
    aux = 0
    copie = nr
    while nr != 0:
        c = nr % 10
        nr = int(nr / 10)
        aux = aux * 10 + c

    if copie == aux:
        return True
    else:
        return False


if __name__ == '__main__':
    print(palindromtuple([121, 23, 34543, 657756, 7, 3, 88]))
