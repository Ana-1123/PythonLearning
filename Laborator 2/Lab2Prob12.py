def group_by_rhyme(list):
    listoflists = []
    for x in list:
        gasit = 0
        if len(listoflists) > 0:
            for y in listoflists:
                for z in y:
                    rhyme = x[-2:]
                    if z[-2:] == rhyme:
                        y.append(x)
                        gasit = 1
                        break
        if gasit == 0:
            curentlist = []
            curentlist.append(x)
            listoflists.append(curentlist)
    return listoflists


if __name__ == '__main__':
    print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))
