import re


def at_least_one(text, expr_list):
    match_list = set()
    for expr in expr_list:
        result = re.findall(expr, text)
        for s in result:
            match_list.add(s)
    return match_list


if __name__ == '__main__':
    print(at_least_one("odfss$ afara 5fab pdsd# pdsd#", ["[0-9].[ab]", "[oip][a-z]+[!@#$%]"]))
