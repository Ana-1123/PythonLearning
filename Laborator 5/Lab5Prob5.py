# Write a function with one parameter which represents a list. The function will return a new list
# containing all the numbers found in the given list.
# Example: my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]) will return [1, 5, 6, 3.0]
import numbers


def my_function(n_list):
    new_list = []
    for element in n_list:
        if isinstance(element, numbers.Number):
            new_list.append(element)
    return new_list


if __name__ == "__main__":
    print(my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
