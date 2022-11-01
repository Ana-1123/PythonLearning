input_string = input("Introduceti sirul de caractere:")
# Metoda 1
new_list = list(filter(lambda c: (c in "aeiouAEIOU"), input_string))
print("Lista obtinuta utilizand metoda 1:", new_list)


# Metoda 2
def vocale(input_s):
    result = []
    for letter in input_s:
        if letter in "aeiouAEIOU":
            result.append(letter)
    print("Lista obtinuta utilizand metoda 2:", result)


# Metoda 3
vocale3 = [letter for letter in input_string if letter in "aeiouAEIOU"]
print("Lista obtinuta utilizand metoda 3:", vocale3)

if __name__ == "__main__":
    vocale(input_string)
