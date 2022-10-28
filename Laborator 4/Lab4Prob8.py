import os


def full(dir_path):
    fullpath = []

    for root, dirs, files in os.walk(dir_path):
        for file in files:
            fullpath.append(os.path.join(dir_path, file))
    return fullpath


if __name__ == '__main__':
    print(full('C:\\Users\\user\\Desktop\\An3Sem1\\Phyton\\directorex5'))
