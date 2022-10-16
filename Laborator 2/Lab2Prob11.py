
def sortlistoftuples(tuples):
    tuples.sort(key=lambda x: x[1][2])
    return tuples


if __name__ == '__main__':
    print(sortlistoftuples([('abc', 'bcd'), ('abc', 'zza')]))
