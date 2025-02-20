# List comprehension cung cấp cho chúng ta cú pháp ngắn hơn để tạo
# list mới dựa trên giá trị của list đã có

# syntax: expression for item in iterable

# Cách tạo list thông thường
lst = [1, 2, 3, 4, 5]
new_lst = []
for x in lst:
    new_lst.append(x ** 2)
print(new_lst)

# List comprehension
lst = [1, 2, 3, 4, 5]
new_lst = [x ** 2 for x in lst]
print(new_lst)

# filter element
# [expression for item in iterable if condition == True]
lst = [1, 2, 3, 4, 5]
new_lst = [x for x in lst if x % 2 == 1]
print(new_lst)

# apply function to each element
# [expression_1 if condition == True else expression_2 for item in iterable]
lst = [1, 2, 3, 4, 5]
new_lst = [x if x % 2 == 0 else x + 2 for x in lst]
print(new_lst)

# dictionary comprehension
# [k: v for item in iterable]
lst = [1, 2, 3, 4, 5]
new_dict = {k: k**2 for k in lst}
print(new_dict)

# set comprehension
# {item for item in iterable}
my_string = "Yutayuyu"
new_set = {letter for letter in my_string}
print(new_set)

# Multiple loops
nested_lst = [[i for i in range(5)] for _ in range(5)]
print(nested_lst)

arr_2d = [
    [1, 2, 3],
    [3, 5, 7],
    [7, 7, 8]
]

# Không nên sử dụng vì khó hiểu
flatten_lst = [num for row in arr_2d for num in row]
print(flatten_lst)

new_lst = []
for row in arr_2d:
    for num in row:
        new_lst.append(num)
print(new_lst)

