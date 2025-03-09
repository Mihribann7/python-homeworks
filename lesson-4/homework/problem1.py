list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

set1 = set(list1)
set2 = set(list2)

list3 = list(set1 ^ set2)
print(list3)
