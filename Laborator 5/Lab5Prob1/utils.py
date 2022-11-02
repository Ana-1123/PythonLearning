# a) Write a module named utils.py that contains one function called process_item.
# The function will have one parameter, x, and will return the least prime number greater than x.
# When run, the module will request an input from the user, convert it to a number and it will display
# the output of the process_item function.
def process_item(x):
    nr = x + 1
    while True:
        ok = 1
        if nr <= 1:
            nr += 1
        for i in range(2, int(nr / 2) + 1):
            if nr % i == 0:
                ok = 0
                nr += 1
                break
        if ok == 1:
            break

    return nr


if __name__ == "__main__":
    x_s = input("Introduceti un numar:")
    x = int(x_s)
    print(process_item(x))
