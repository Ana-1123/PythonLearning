# a) Write a function called print_arguments with one parameter named function.
# The function will return one new function which prints the arguments and the keyword
# arguments received and will return the output of the function receives as a parameter.

def multiply_by_two(x):
    return x * 2


def add_numbers(a, b):
    return a + b


def print_arguments(function):
    def new_function(*args, **kwargs):
        print("Arguments are:", args,",", kwargs)
        return function(*args, **kwargs)

    return new_function


if __name__ == "__main__":
    augmented_multiply_by_two = print_arguments(multiply_by_two)
    x = augmented_multiply_by_two(10)  # this will print: Arguments are: (10,), {} and will return 20.
    print(x)
    augmented_add_numbers = print_arguments(add_numbers)
    x = augmented_add_numbers(3, 4)  # this will print: Arguments are: (3, 4), {} and will return 7.
    print(x)


# b) Write a function called multiply_output with one parameter named function.
# The function will return one new function which returns the output of the
# function received multiplied by 2.
def multiply_by_three(x):
    return x * 3


def multiply_output(function):
    def new_function(*args, **kwargs):
        return 2 * function(*args, **kwargs)

    return new_function


augmented_multiply_by_three = multiply_output(multiply_by_three)
x = augmented_multiply_by_three(10)  # this will return 2 * (10 * 3)
print(x)


# c)
def augment_function(function, decorators):
    def new_function(*args, **kwargs):
        result = function
        for f in decorators:
            result = f(result)
        return result(*args, **kwargs)

    return new_function


decorated_function = augment_function(add_numbers, [print_arguments, multiply_output])
x = decorated_function(3, 4)  # this will print: Arguments are: (3, 4), {} and will return (2 * (3 + 4))
print(x)
