org_list = [11, 56, 10, 349, 0, 35, 12, 95, 23, 656]
new_list = [org_list[i] for i in range(1,len(org_list)) if org_list[i] > org_list[i-1]]
print(new_list)