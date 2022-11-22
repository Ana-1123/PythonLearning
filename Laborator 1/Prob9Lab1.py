def common_letter(text):
    text = text.lower()
    counter = dict()
    for character in text:
        if character.isalpha():
            if character not in counter.keys():
                counter.update({character: 1})
            else:
                c = counter.get(character) + 1
                counter.update({character: c})
    c_letter = max(counter, key=counter.get)
    print(c_letter)
    print(counter)


if __name__ == '__main__':
    common_letter("an apple is not a tomato")
