# Write a function that receives as a parameter a list and returns a tuple (a, b),
# representing the number of unique elements in the list, and b representing
# the number of duplicate elements in the list (use sets to achieve this objective).

def uniqueduplicate(list):
    # a = 0
    # b = 0
    # # llist=len(list)
    # u = set(list)
    # # lset=len(u)
    # for i in u:
    #     if list.count(i) > 1:
    #         b = b + 1
    #     else:
    #         a = a + 1
    # return (a, b)
    # # return (lset,llist-lset)
    aset = set(filter(lambda element: list.count(element) == 1, list))
    bset = set(filter(lambda element: list.count(element) > 1, list))
    return (len(aset), len(bset))


if __name__ == '__main__':
    print(uniqueduplicate([2, 2, 3, 1, "sfsd", 'd', 'd', "d", 4, 5]))
