# 3.Compare two dictionaries without using the operator "==" returning True or False.
def compare(d1, d2):
    if len(d1.items()) != len(d2.items()):
        return False
    for k1 in d1.keys():
        ok = 0
        for k2 in d2.keys():
            if k1 is k2:
                ok = 1
                if d1.get(k1) is not d2.get(k2):
                    return False
        if ok == 0:
            return False
    return True


if __name__ == '__main__':
    print(compare({
        "key1": "come inside, it's too cold out", 3: 2}, {
        "key1": "come inside, it's too cold out", "key3": "this is not valid"}))
