my_list = [1, 2, 3, 4, 5]
# for
for item in my_list:
    print(item)

for i in range(len(my_list)):
    print(f"{i}: {my_list[i]}")

# while
# condition = True
# while condition:
#     pass
count = 1
while count < 5:
    print(count)
    count += 1

# break, countinue
for item in my_list:
    # print(item)
    if item == 3:
        # break
        continue
    print(item)