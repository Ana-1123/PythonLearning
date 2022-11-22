def uppertolower(cuvant):
    for c in cuvant:
        if c in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            cuvant = cuvant.replace(c, '_' + c)
    cuvant = cuvant.lower()
    cuvant = cuvant[1:len(cuvant)]
    print(cuvant)


if __name__ == '__main__':
    uppertolower('AziELuni')
