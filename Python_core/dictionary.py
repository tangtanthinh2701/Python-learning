# 1. Định nghĩa
# Dictionary là một data collection được lưu dưới dạng map

# Khởi tạo dictionary
name_age = {"Ban": 5, "Na": 6, "Can": 10}
# Tạo dictionary rỗng
# your_name = dict()
# first_name = {}

# Truy cập
print(name_age["Na"])

# Thêm vào dict, update giá trị
name_age["Can"] = 12
print(name_age)
name_age["Bo"] = 30
print(name_age)

# Duyệt qua các phần tử của dictionary

# Duyệt qua các keys
for k, v in name_age.items():
    print(k, v)
# for k in name_age:
#     print(k)
for k in name_age.keys():
    print(k)

# Duyệt qua các values
for v in name_age.values():
    print(v)

