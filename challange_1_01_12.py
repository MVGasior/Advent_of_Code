#First challange from advent calendar (01.12.2020)
#Author: Matuesz Gąsior

number_list = []
with open("input") as file:
    for word in file:
        number_list.append(word[:-1])

for num in number_list:
    check_num = number_list.pop(0)
    for add_num in number_list:
        for next_num in number_list[number_list.index(add_num):]:
            if int(check_num) + int(add_num) + int(next_num) == 2020:
                print(check_num)
                print(add_num)
                print(next_num)
                print(int(check_num) * int(add_num) * int(next_num))