import os


def byte_converter(size):
    units = ["Bytes", "KBytes", "MBytes", "GBytes"]
    counter = 0
    while size // 1024 > 0:
        counter += 1
        size //= 1024
    return size, units[counter]


for currentdir, dirs, files in os.walk('.'):
    for file in files:
        print(file, byte_converter(os.path.getsize(fr"{currentdir}\{file}")))