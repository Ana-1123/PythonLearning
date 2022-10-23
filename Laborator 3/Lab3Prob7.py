def ex7(*sets):
    dictionary = {}
    for i in range(0, len(sets)):
        for j in range(i + 1, len(sets)):
            dictionary[str(sets[i]) + " | " + str(sets[j])] = sets[i].union(sets[j])
            dictionary[str(sets[i]) + " & " + str(sets[j])] = sets[i].intersection(sets[j])
            dictionary[str(sets[i]) + " - " + str(sets[j])] = sets[i].difference(sets[j])
            dictionary[str(sets[j]) + " - " + str(sets[i])] = sets[j].difference(sets[i])
    return dictionary


if __name__ == '__main__':
    print(ex7({1, 2}, {2, 3}))
