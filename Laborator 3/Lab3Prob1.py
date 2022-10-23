#1.Write a function that receives as parameters two lists a and b and returns a list of sets containing:
# (a intersected with b, a reunited with b, a - b, b - a)
def twoList(a, b):
    return [set(a).intersection(b), set(a).union(b), set(a).difference(b), set(b).difference(a)]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(twoList([34, 4, 1, 4, 9, 5, 7, 345], [2, 4, 7, 5, 8, 3, 9, 12, 84, 7]))