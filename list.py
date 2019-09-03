x=['5','6','100','34','56','67','67','8','4','6']
new_list=[]
print(x)
for i in x:
        if i not in new_list:
                new_list.append(i)
print(new_list)
