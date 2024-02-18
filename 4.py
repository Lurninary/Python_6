import shutil
import os
from datetime import datetime


def make_reserve_arc(source, dest):
    if not os.path.exists(source):
        print("Исходный каталог не существует.")
        return
    if not os.path.isdir(source):
        print("Исходный путь не является каталогом.")
        return

    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    arc_name = f"archive_{current_time}.zip"
    arc_path = os.path.join(dest, arc_name)

    try:
        shutil.make_archive(arc_path[:-4], 'zip', source)
        print(f"Архив успешно создан: {arc_path}")
    except Exception as e:
        print(f"Ошибка при создании архива: {e}")


source_dir = input("Введите путь к исходному каталогу: ")
dest_dir = input("Введите путь к каталогу для сохранения архива: ")

make_reserve_arc(source_dir, dest_dir)