# Write a function that receives as a parameter a variable number of lists and a whole number x.
# Return a list containing the items that appear exactly x times in the incoming lists.

def appear(x, *lists):
    hashmap = {}
    xtimesappear = []
    for list in lists:
        for item in list:
            if item in hashmap:
                k = hashmap.get(item)
                k = k + 1
                hashmap[item] = k
            else:
                hashmap[item] = 1
    for key in hashmap.keys():
        if hashmap.get(key) == x:
            xtimesappear.append(key)
    return xtimesappear


if __name__ == '__main__':
    print(appear(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))
