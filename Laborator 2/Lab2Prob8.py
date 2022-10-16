# Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag
# set to True. For each string, generate a list containing the characters that have the ASCII code
# divisible by x if the flag is set to True, otherwise it should contain characters that have the ASCII
# code not divisible by x

def asciidiv(x, list, flag):
    finallist = []
    for s in list:
        curentlist = []
        for c in s:
            if flag == True:
                if ord(c) % x == 0:
                    curentlist.append(c)
            else:
                if ord(c) % x != 0:
                    curentlist.append(c)
        if len(curentlist) > 0:
                finallist.append(curentlist)
    return finallist


if __name__ == '__main__':
    print(asciidiv(2, ["test", "hello", "lab002"], False))
