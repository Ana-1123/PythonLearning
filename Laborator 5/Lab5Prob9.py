def f9(pairs):
    result = []
    for pair in pairs:
        result.append({"sum": pair[0] + pair[1],
                       "prod": pair[0] * pair[1],
                       "pow": pair[0] ** pair[1]})
    return result


if __name__ == '__main__':
    print(f9(pairs=[(5, 2), (19, 1), (30, 6), (2, 2)]))
    # will return [{'sum': 7, 'prod': 10, 'pow': 25}, {'sum': 20, 'prod': 19, 'pow': 19},
    # {'sum': 36, 'prod': 180, 'pow': 729000000}, {'sum': 4, 'prod': 4, 'pow': 4}]
