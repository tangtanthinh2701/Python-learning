my_Str = "Hello Python"
print(my_Str)
print(type(my_Str))

# Length of a string
print(len(my_Str))

# index in string
# index dương: 0 => len(str) - 1
print(my_Str[0])
print(my_Str[len(my_Str) - 1])

# index âm:
print(my_Str[-1])
print(my_Str[-2])

# Slicing for string
# index: 1, 2, 3
print(my_Str[1:4])
# index: 1 to n - 1
print(my_Str[1:])
# không bao gồm index n - 1
print(my_Str[:-1])

# concat in python
str1 = "Master"
str2 = "Python"
concat_str = str1 + " " + str2
words = ["Hello", "World", "Python"]
result = " ".join(words)
usingJoin = " ".join([str1, str2])
print(concat_str)
print(result)
print(usingJoin)

name = "Yutayuyu"
example = "Hello, {}!".format(name)
print(example)

name = "Python"
fstrings = f"Hello, {name}!"
print(fstrings)

# Duyệt qua các ký tự trong string
loopString = "Yutayuyu2701"
for char in loopString:
    print(char)

# Kiểm tra chuỗi con có nằm trong chuỗi hay không?
checkString = "Hello, I'm yuta"
if "yuta" in checkString:
    print("Oke")
else:
    print("No")

# Methods
methodString = "Check method in Python"
print(methodString.upper())
print(methodString.lower())

# String is immutable in Python
myString = "Hello everyone"
# myString[1] = "E" // Error
print(myString)
myString = "Bye bitch!"
print(myString)
