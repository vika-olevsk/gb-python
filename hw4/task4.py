org_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in org_list if org_list.count(el) < 2]
print(new_list)