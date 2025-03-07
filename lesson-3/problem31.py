my_list = [1, 5, 3, 9, 2, 8]
repeat = 3
new_list = [x for x in my_list for _ in range(repeat)]
print(new_list)  