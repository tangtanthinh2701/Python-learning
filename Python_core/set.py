# Khái niệm
# 1. Tạo Set
my_set = {'a', 'b'}
print(my_set, type(my_set))
empty_set = set()
print(empty_set, type(empty_set))

# 2. Không cho phép các phần tử lặp lại
unique_set = {'a', 'b', 'c', 'a', 'b', 'c'}
print(unique_set)

# 3. Check set là unorder (Mỗi lần chạy lại thứ tự sẽ khác nhau)
loop_set = {'a', 'b', 'c', 'd', 'e', 'f'}
for item in loop_set:
    print(item)

# 4. Update set (Hay sử dụng thêm vào set)
update_set = {'a', 'b', 'c', 'd'}
update_set.add('e')
print(update_set)
update_set.discard('a')
print(update_set)

# Thao tác với 2 hay nhiều sets, xem thêm sơ đồ Venn
my_set_1 = {'a', 'b', 'c', 'd'}
my_set_2 = {'a', 'b', 'c', 'd', 'e', 'f'}
# Giao
new_set = my_set_1.intersection(my_set_2)
print(new_set)

# Hợp
new_set = my_set_1.union(my_set_2)
print(new_set)

# Phần tử chỉ có ở A mà không có ở B và ngược lại
new_set = my_set_1.symmetric_difference(my_set_2)
print(new_set)
