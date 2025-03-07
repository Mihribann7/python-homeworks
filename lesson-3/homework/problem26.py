my_list = [1, 2, 3, 4, 5, 6]
length = len(my_list)
mid = length // 2

middle = my_list[mid] if length % 2 != 0 else [my_list[mid - 1], my_list[mid]]
print(middle)
