def my_function(*p, **k):
    c = 0
    for i in p:
        for j in k:
            if i == k[j]:
                c = c + 1
    return c


if __name__ == '__main__':
    print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))
