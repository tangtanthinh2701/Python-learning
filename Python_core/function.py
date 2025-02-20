# def my_sum(x, y):
#     return x + y
#
# def my_func(x, y):
#     print(f"So thu nhat la {x}, so thu hai la {y}")
#
# a = 5
# b = 6
# print(my_sum(a, b))
# print(my_sum(1, 2))
# my_func(1, 2)

import shutil
import os


def copy_func(source_dir, des_dir):
    list_name = os.listdir(source_dir)
    for file_name in list_name:
        shutil.copy(os.path.join(source_dir, file_name), os.path.join(des_dir, file_name))


source_dir = "source_dir"
des_dir = "des_dir"
copy_func(source_dir, des_dir)

