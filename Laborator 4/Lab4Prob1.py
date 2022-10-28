import os


def list_of_unique_extensions(director):
    unique_extensions = set()

    for root, dirs, files in os.walk(director):
        for file in files:
            pathname, extension = os.path.splitext(file)
            unique_extensions.add(extension)
    return sorted(list(unique_extensions))


if __name__ == '__main__':
    print(list_of_unique_extensions('C:\\Users\\user\\Desktop\\An3Sem1\\Phyton\\directorEx1'))
