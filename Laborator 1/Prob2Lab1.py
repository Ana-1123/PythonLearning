def num_vocale(cuvant):
    nr_vocale = 0
    for c in cuvant:
        if c in "aeiouAEIOU":
            nr_vocale = nr_vocale + 1
    return nr_vocale


if __name__ == '__main__':
    print(num_vocale('Afara'))
