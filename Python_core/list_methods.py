# Methods of list
my_list = [1, 3, 6, 10, -5]

# 1. Add list element (1 element)
# .append()
my_list.append(50)
print(my_list)

# 2. Add elements
# .extend()
my_list1 = [1, 2, 3]
my_list1.extend([4, 5])
print(my_list1)
list_1 = [1, 2.5, 30, 67, -1.5]
list_2 = ["hello", "world"]  # general: iterable
list_1.extend(list_2)
print(list_1)

# 3. sort list
# .sort() or sorted()
list_3 = [1, 2.5, 30, 67, -1.5]
list_3.sort()
print(list_3)
list_3.sort(reverse=True)
print(list_3)
new_list = sorted(list_3)  #list_3 không thay đổi
print(list_3)
print(new_list)

# 4. Reverse list
list_4 = [-1, 2.5, 30, 67, -1.5]
new_lst = list_4[::-1]  # (slicing) start:stop:step
print(new_lst)
list_4.reverse()
print(list_4)

# 5. Insert element
# .insert(index, value)
list_5 = [1, 3, 6, 10, -56]
list_5.insert(0, 100)
print(list_5)
list_5.insert(1, 2.2)
print(list_5)

# 6. Delete element
# del or .remove(ele)

list_6 = [1, 3, 6, 10, -56]
# del list_6[len(list_6) - 1]
del list_6[:2]
print(list_6)
list_6.remove(-56)
print(list_6)

# 7. Trả về index đầu tiên của element được khớp .index() (không có error)
# Phương thức được sử dụng để trả về chỉ số của phần tử đầu tiên xuất hiện trong danh sách
list_7 = [1, 3, 6, 10, -5, 33, -5]
ind = list_7.index(-5)
print(ind)

# 8. pop(index) không truyền xóa element cuối
list_8 = [1, 3, 6, 10, -5]
ele = list_8.pop(3)
print(ele)
print(list_8)