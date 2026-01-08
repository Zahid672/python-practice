speed = {'jan': 47, 'feb': 52, 'march': 47, 'april': 44, 'may': 52, 'june': 53, 'july': 54, 'aug': 44, 'sep': 54}
# unique_speeds = list(set(speed.values()))
# print("Unique speeds:", unique_speeds)

speed_list = list()
for value in speed.values():
    if value not in speed_list:
        speed_list.append(value)
print("Unique speeds:", speed_list)