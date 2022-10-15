# Cerinta: Write a function to return a list of the first n numbers in the Fibonacci string.

def fibonacci(n):
    lista = []
    a = 1
    b = 1
    lista.append(1)
    lista.append(1)
    for i in range(2, n):
        c = a + b
        lista.append(c)
        a = b
        b = c
    return lista


if __name__ == '__main__':
    print(fibonacci(6))
