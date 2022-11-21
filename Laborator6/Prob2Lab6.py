import re


def match_expr(regex, text, x):
    substrings = []
    result = re.findall(regex, text)
    for substring in result:
        if len(substring) == x:
            substrings.append(substring)
    return substrings


if __name__ == '__main__':
    print(match_expr(r"\w+[025]", "textul0 pentru proble5/exercitiul 2 din laboratorul 2", 7))
