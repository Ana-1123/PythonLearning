import os
import sys

def argv_example():
    myPath = sys.argv[1]
    unique_extensions = set()

    for file in os.listdir(myPath):
        pathname, extension = os.path.splitext(file)
        unique_extensions.add(extension)
    return sorted(list(unique_extensions))


if __name__ == '__main__':
    print(argv_example())
