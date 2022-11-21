import re


def xml_attr(path, attrs):
    f = open(path, "rt")
    content = f.read()
    elements = set()
    for key, value in attrs.items():
        s = r"(\s+" + key + r"\s*=\s*\"" + value + r"\"\s*)"
        s = "(<)([a-zA-z]+).*(" + s + r")(\s*)"
        r = re.compile(s)
        if len(elements) > 0:
            have_attr = set()
            for x in r.findall(content):
                have_attr.add(x[1])
            elements = elements.intersection(have_attr)
        else:
            for x in r.findall(content):
                elements.add(x[1])
    f.close()
    return elements


if __name__ == '__main__':
    print(xml_attr("exemplu.xml", {"class": "url", "name": "url-form", "data-id": "item"}))
