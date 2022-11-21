import re


def extract(text):
    result = re.findall(r"\w+", text)
    if result:
        return result


if __name__ == '__main__':
    print(extract('dasfds2 3 ^ sdfserw3r2 f 123 '))
