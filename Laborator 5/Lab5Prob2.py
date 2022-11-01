# 1
def my_function(*args, **kwargs):
    suma = 0
    for key, value in kwargs.items():
        suma += value
    return suma


# 2
l_sum = lambda *args, **kwargs: sum(kwargs.values())

if __name__ == "__main__":
    print("Suma obtinuta utilizand functie:", my_function(1, 2, c=3, d=4))
    print("Suma obtinuta utilizand functie anonima:", l_sum(1, 2, c=3, d=4))
