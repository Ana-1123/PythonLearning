import os


def write(director, fisier):
    try:
        filetowrite = open(fisier, 'w')
        for root, dirs, files in os.walk(director):
            for file in files:
                if file.startswith("A"):
                    copy_buffer = os.path.join(root, file) + '\n'
                    if not copy_buffer:
                        break
                    filetowrite.write(copy_buffer)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    write('C:\\Users\\user\\Desktop\\An3Sem1\\Phyton\\directorEx1',
          'C:\\Users\\user\\Desktop\\An3Sem1\\Phyton\\filepath.txt')
