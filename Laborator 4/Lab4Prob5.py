import os


def fileordirectory(target, to_search):
    listoffiles = []
    try:
        if os.path.isfile(target):
            openfile = open(target, "rt").read()
            if openfile.count(to_search) > 0:
                listoffiles.append(target)
            return listoffiles
        elif os.path.isdir(target):
            for root, dirs, files in os.walk(target):
                for file in files:
                    f = os.path.join(target, file)
                    openfile = open(f, 'rt').read()
                    if openfile.count(to_search) > 0:
                        listoffiles.append(file)
            return listoffiles
        else:
            raise ValueError("Stringul dat nu contine o cale nici de fisier nici de director")
    except Exception as e:
        return e


if __name__ == '__main__':
    print(fileordirectory('C:\\Users\\user\\Desktop\\An3Sem1\\Phyton\\directorex5', 'vreme'))
