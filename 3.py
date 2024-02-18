import os


def get_dir_size(dir_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            if not os.path.islink(file_path):
                total_size += os.path.getsize(file_path)
    return total_size


def byte_converter(size):
    units = ["Bytes", "KBytes", "MBytes", "GBytes"]
    counter = 0
    while size // 1024 > 0:
        counter += 1
        size //= 1024
    return size, units[counter]


dir_sizes = {}

for dirpath, dirnames, filenames in os.walk('.'):
    for file in filenames:
        dir_sizes[file] = os.path.getsize(fr"{dirpath}\{file}")
    for dir in dirnames:
        dir_sizes[dir] = get_dir_size(dir)
    break

sorted_dir_sizes = sorted(dir_sizes.items(), key=lambda x: x[1], reverse=True)

for item in sorted_dir_sizes[:10]:
    size, unit = byte_converter(item[1])
    print(f"{item[0]}: {size} {unit}")