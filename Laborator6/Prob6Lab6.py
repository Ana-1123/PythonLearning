import re


def censures(text):
    result = re.findall(r"\b[aeiouAEIOU]\w+[aeiouAEIOU]\b", text)
    list_words = []
    for s in result:
        current = list(s)
        for i in range(0, len(current), 2):
            current[i] = "*"
        new = ''.join(current)
        list_words.append(new)
    return list_words


if __name__ == '__main__':
    print(censures("inlocuieste vocale afara este nins"))
