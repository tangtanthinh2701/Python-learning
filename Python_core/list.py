# empty list
empty_List = []
empty_lst = list()
print(empty_List)
print(empty_lst)

my_List = [12, 3.5, "string", [5, 7]]
print(my_List)
print(my_List[len(my_List) - 1])
print(len(my_List))
print(type(my_List))
print(my_List[0])
print(my_List[1])
print(my_List[-1])
print(my_List[1:])
print(my_List[:-1])

for x in my_List:
    print(x)

list_1 = [1, 4.5, 10]
list_2 = ["test", "example"]
concat_list = list_1 + list_2
print(concat_list)

lists = [1, 4.5, 10]
print(lists)
lists[1] = "hello"
print(lists)