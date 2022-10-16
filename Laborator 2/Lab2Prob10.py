def listoftuples(*lists):
    tlist = []
    length = max([len(k) for k in lists])

    for i in range(0, length):
        plist = []
        for list in lists:
            plist.append(list[i])
        tlist.append(tuple(plist))
    return tlist


if __name__ == '__main__':
    print(listoftuples([1, 2, 3], [5, 6, 7], ["a", "b", "c"]))
