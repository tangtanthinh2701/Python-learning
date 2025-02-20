# File handling in Python
# Overview:
# Function open(), 2 parameters: filename, and mode
# - 4 modes for opening file:
#     - "r" - Read - Default value, error if the file does not exist
#     - "a" - Append, creates the file if it does not exist
#     - "w" - Write, creates the file if it does not exist
#     - "x" - Create, returns an error if the file exists
# - File should be handled as binary or text mode:
#     - "t" - Text - Default value. Text mode
#     - "b" - Binary - Binary mode

# Read
file_obj = open("my_file.txt") #rt
content = file_obj.read()
print(content)
file_obj.close()

# Context manager
with open("my_file.txt") as file_obj:
    content = file_obj.read()  # .readline(), .readlines()
    print(content)
    print(file_obj.read())

# Write - "w"
with open("new_file.txt", "w") as f:
    f.write("I work as an AI engineer!")

# Append - "a"
with open("new_file.txt", "a") as f:
    f.write("\nI love my job!")

# Create - "x"
with open("file_1.txt", "x") as f:
    pass