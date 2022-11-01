def my_function(*args, **kwargs):
    list_of_dict = []
    for e in args:
        if type(e) is dict:
            found = 0
            if len(e.keys()) >= 2:
                for k in e.keys():
                    if type(k) is str and len(k) >= 3:
                        found = 1
            if found == 1:
                list_of_dict.append(e)
    for key, value in kwargs.items():
        if type(value) is dict:
            found = 0
            if len(value.keys()) >= 2:
                for k in value.keys():
                    if type(k) is str and len(k) >= 3:
                        found = 1
            if found == 1:
                list_of_dict.append(value)

    return list_of_dict


if __name__ == "__main__":
    print(my_function({1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': 5},
                      3764, dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True}))
