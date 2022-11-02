# Write a function that receives a list with integers as parameter that contains an equal number
# of even and odd numbers that are in no specific order. The function should return a list of pairs
# (tuples of 2 elements) of numbers (Xi, Yi) such that Xi is the i-th even number in the list and Yi is
# the i-th odd number
# my_function([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]) will return [(2, 1), (8, 3), (4, 5), (10, 7), (2, 9)]

def my_function(n_list):
    new_list = []
    even_list = []
    odd_list = []
    for element in n_list:
        if element % 2 == 0:
            even_list.append(element)
        else:
            odd_list.append(element)
    for i in range(0, len(even_list)):
        new_list.append((even_list[i], odd_list[i]))
    return new_list


if __name__ == "__main__":
    print(my_function([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))
