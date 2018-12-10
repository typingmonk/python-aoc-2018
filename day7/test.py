name_list = []
for i in range(5):
    name_list.append({"name":""})

for name_dict in name_list:
    name_dict["name"] = "Felix"
    print("Here")
    break
print(name_list)