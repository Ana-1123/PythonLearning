def sum_digits(x):
    return sum(map(int, str(x)))


def process(**kwargs):
    fibo = [1, 1]
    for i in range(2, 100):
        fibo.append(fibo[i - 2] + fibo[i - 1])

    for key, value in kwargs.items():
        if key == "filters":
            for predicate in value:
                fibo = list(filter(predicate, fibo))
        if key == "offset":
            fibo = fibo[value:]
        if key == "limit":
            fibo = fibo[:value]
    return fibo


if __name__ == "__main__":
    print(process(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
                  offset=2, limit=2))
