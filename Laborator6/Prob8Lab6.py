import re
import os


def files_check(directory, expr):
    for (root, directories, files) in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            name, extension = file.split('.')
            f = open(file_path, "rt")
            content = f.read()
            if re.match(expr, str(name)) and re.match(expr, content):
                print("<<" + file_path)
            elif re.match(expr, str(name)) or re.match(expr, content):
                print(file_path)
            f.close()


if __name__ == '__main__':
    files_check("C:\\Users\\Ana\\Desktop\\An3Sem1\\Phyton\\directorex8", r"\b[AB]\w+[w3]\b")
