import re


def xml_attr(path, attrs):
    f = open(path, "rt")
    content = f.read()
    elements = set()
    for key, value in attrs.items():
        s = r"(\s+" + key + r"\s*=\s*\"" + value + r"\"\s*)"
        s = "(<)([a-zA-z]+).*(" + s + r")(\s*>)"
        for x in re.findall(s, content):
            elements.add(x[1])
    f.close()
    return elements


if __name__ == '__main__':
    print(xml_attr("exemplu.xml", {"class": "url", "name": "url-form", "data-id": "item"}))
