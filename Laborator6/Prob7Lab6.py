import re
#S-[1-8] AA-oricare 2 cifre LL-luna ZZ-ziua JJJ NNN C

def is_cnp(text):
    if re.match(r"[1-8][0-9]{2}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[10])[0-9]{6}", text):
        return "Este CNP"
    return "Nu este CNP"


if __name__ == '__main__':
    print(is_cnp('1460913400088'))
