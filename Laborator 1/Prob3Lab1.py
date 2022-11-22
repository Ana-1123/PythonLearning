def occurence(str1, str2):
    return len(str2.split(str1)) - 1


if __name__ == '__main__':
    print(occurence('ala', 'ala bala portocal'))
