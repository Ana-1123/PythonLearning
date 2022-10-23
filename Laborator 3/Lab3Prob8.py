def loop(d):
    list = []
    list.append(d.get('start'))
    currentkey = d.get('start')
    while d.get(currentkey) not in list:
        list.append(d.get(currentkey))
        currentkey = d.get(currentkey)
    return list


if __name__ == '__main__':
    print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
