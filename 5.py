from zipfile import ZipFile
import json


def counter(path):
    count = 0

    with ZipFile(path, 'r') as myzip:
        for filename in myzip.namelist():
            if filename.endswith(".json"):
                with myzip.open(filename) as file:
                    data = json.load(file)
                    if data['city'] == "Moscow":
                        count += 1
                        print(file.name)

    return count


print("Count: ", counter(r"task5.zip"))
