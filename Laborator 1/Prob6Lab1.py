def palindrom(nr):
    aux = 0
    copie = nr
    while nr != 0:
        c = nr % 10
        nr = int(nr / 10)
        aux = aux * 10 + c

    if copie == aux:
        print('Este palindrom')
    else:
        print('Nu este palindrom')


if __name__ == '__main__':
    palindrom(11211)
