#2. Write a function that receives a string as a parameter and returns a dictionary in which the keys are the
# characters in the character string and the values are the number of occurrences of that character in the given text.

def dictionary(string):
    dict = {}
    for char in string:
        if dict.get(char) is not None:
            dict[char] = dict.get(char) + 1
        else:
            dict[char] = 1
    return dict


if __name__ == '__main__':
    print(dictionary("Ana has apples."))