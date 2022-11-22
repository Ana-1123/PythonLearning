def nr_bits(nr):
    nr = str(bin(nr))
    k = 0
    for i in nr:
        if i == "1":
            k += 1
    return k


if __name__ == '__main__':
    print(nr_bits(24))
