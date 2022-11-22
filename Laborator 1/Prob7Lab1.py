def extractnumber(cuvant):
    numar = []
    for i in range(0, len(cuvant)):
        if cuvant[i].isdigit() is True:
            break
    while cuvant[i].isdigit() is True:
        numar.append(cuvant[i])
        i = i + 1
    print(''.join(numar))


if __name__ == '__main__':
    extractnumber("An apple is 123 USD")
