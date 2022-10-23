def validate_dict(s, d):
    if len(s) != len(d.keys()):
        return False

    for rule in s:
        prefix = str(rule[1])
        middle = str(rule[2])
        suffix = str(rule[3])
        value = str(d.get(rule[0]))
        if (value.startswith(prefix) and value.endswith(suffix) and middle in value) is not True:
            return False

    return True


if __name__ == '__main__':
    print(validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}, {
        "key1": "come inside, it's too cold out", "key3": "this is not valid"}))
