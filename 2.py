from zipfile import ZipFile
import os


def byte_converter(size):
    map = {0: "Bytes", 1: "KBytes", 3: "MBytes", 4: "GBytes"}
    counter = 0
    while size // 1024 > 0:
        counter += 1
        size //= 1024
    return f"{size} {map[counter]}"


with ZipFile("BSL_v8.1.02.2.zip", "r") as myzip:
    for item in myzip.infolist():
        if item.is_dir():
            step = '    ' * (item.filename.count('/') - 1)
            print(step + item.filename)
        else:
            step = '    ' * item.filename.count('/')
            print(step + os.path.basename(item.filename), byte_converter(item.file_size))