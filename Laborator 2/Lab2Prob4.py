
def compose(notes, moves, start):
    melodie = []
    melodie.append(notes[start])
    for i in moves:
        k = start + i
        start = k
        melodie.append(notes[k])
    return melodie


if __name__ == '__main__':
    print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, -3], 2))
