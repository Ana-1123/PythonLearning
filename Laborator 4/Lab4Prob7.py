import os


def get_file_info(path):
    try:
        info = {"full_path": os.path.abspath(path), "file_size": os.path.getsize(path),
                "file_extension": os.path.splitext(path)[1], "can_read": os.access(path, os.R_OK),
                "can_write": os.access(path, os.W_OK)}
    except Exception as e:
        return e
    return info


print(get_file_info("C:\\Users\\user\\Desktop\\An3Sem1\\Phyton\\directorex5\\tfh.txt"))
