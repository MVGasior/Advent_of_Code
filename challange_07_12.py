# Seventh challange from advent calendar (07.12.2020)
# Author: Matuesz Gąsior


list_of_index = []
values = []
bags = []
for line in open('input_07_12'):
    title = line.split(' contain ')
    list_of_index.append(title[0].split('bags')[0])
    value = title[1].replace('.\n', '').replace('bags', '').replace('bag', '').replace('no other ', '').split(', ')
    values.append(value)

for bag in values:
    temp_dict = {}
    for i in bag:
        if i != '':
            temp_dict[i[2:]] = i[0]
        else:
            temp_dict = {'': 0}
    bags.append(temp_dict)

dict_of_bags = {list_of_index[ind]: bags[ind] for ind in range(len(list_of_index))}
bagging = ['shiny gold ']
num = 0
for pos in bagging:
    for i in dict_of_bags.items():
        k = i[0]
        list_of_bags = list(i[1].keys())
        if pos in list_of_bags and k not in bagging:
            num += 1
            bagging.append(k)


def many_bags(name):
    value_steps = []
    if name == '':
        return 0
    else:
        for n in dict_of_bags[name].items():
            value_steps.append(many_bags(n[0]) * int(n[1]) + int(n[1]))
        return sum(value_steps)


print(many_bags('shiny gold '))
bagging.sort()
print(bagging)

