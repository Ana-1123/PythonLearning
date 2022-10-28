import os


def fileordirectory(my_path):
    if os.path.isfile(my_path):
        data = open(my_path, "rt").read()
        return data[-20:]
    elif os.path.isdir(my_path):
        extcount = {}
        for root, dirs, files in os.walk(my_path):
            for file in files:
                pathname, extension = os.path.splitext(file)
                if extension not in extcount.keys():
                    extcount.update({extension: 1})
                else:
                    extcount.update({extension: extcount.get(extension) + 1})
        return extcount
    else:
        print("Stringul dat nu contine o cale nici de fisier nice de director")


if __name__ == '__main__':
    print(fileordirectory('C:\\Users\\user\\Desktop\\An3Sem1\\Phyton\\directorEx1'))
