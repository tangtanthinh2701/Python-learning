# Tuple in Python

# 1. Create a tuple
# Để tạo 1 tuple có 1 phần tử ta cần khai báo như sau
# tuple = ("1",)  // Tạo tuple có một phần tử
# Nếu không có dấu phẩy Python sẽ tự xác định ta đang khai báo một đối tượng có kiểu dữ liệu nguyên thủy
tuple_1 = ("a", 3)
print(tuple_1)
print(type(tuple_1))

# 2. Duyệt qua các phần tử của Tuple
tuple_2 = ("a", 3, 4, "b")
print(f"Chiều dài của tuple: {len(tuple_2)}")

for item in tuple_2:
    print(item)

# Truy xuất phần tử trong tuple ta cũng sử dụng index như list
print(tuple_2[1])

# 3. Cộng các tuples
tuple_a = ("a", 3, 4, "b")
tuple_b = ("a32", 57, 92, "b52")
new_tuple = tuple_a + tuple_b
print(f"New tuple: {new_tuple}")

# Python không hỗ trợ các method xử lý thêm sửa xóa trên tuple
# Nên khi cần thực hiện các thao tác trên ta convert nó sang list sau đó convert lại tuple
tuple_3 = ("abc", 3.14, 8386, "edf")
list_1 = list(tuple_3)  # ['abc', 3.14, 8386, 'edf']
# list_1.append("hello")
list_1.remove(3.14)
new_tuple_1 = tuple(list_1)
print(f"new_tuple: {new_tuple_1}")

# Method in tuple
tuple_4 = ("abc", 3.14, 8386, "edf")
print(tuple_4.count(8386))
print(tuple_4.count(82))
print(tuple_4.index("edf"))

# Tuple is immutable
tuple_5 = ("a", 3, 4, "b", "a")
tuple_6 = ("a", 3, 4, "b", "a")
# Cả 2 id như nhau => tính chất immutable (Nhưng list sẽ khác nhau)
print(f"ID of tuple 5: {id(tuple_5)}")
print(f"ID of tuple 6: {id(tuple_6)}")

# Trong tuple có một phần tử có tính chất mutable thì ta cũng không thể nào thay đổi giá trị của phần từ mutable
# bằng cách gán thẳng nó mà ta cần phải chỉ đúng index mới thay đổi được
tuple_7 = ([1, 2, 3], 3, 4, "edf")
print(tuple_7)
# Error
# tuple_7[0] = [0, 2, 3]

# Correct
tuple_7[0][0] = 0
print(tuple_7)
