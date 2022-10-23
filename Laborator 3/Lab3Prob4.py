def build_xml_element(tag, content, href, _class, id):
    return "<" + tag + " href=\"" + href + "\" _class=\"" + _class + "\" id=\"" + id + "\">" + content + "</" + tag + ">"


if __name__ == '__main__':
    print(build_xml_element("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid "))

#"<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"