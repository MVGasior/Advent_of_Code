# Ninth challange from advent calendar (09.12.2020)
# Author: Matuesz Gąsior

list_of_numbers = []
for line in open('input_09_12'):
    list_of_numbers.append(int(line))


def checking_xmas_encryption(list_of_numbers):
    for i in range(len(list_of_numbers[24:])-1):
        temp_list = list_of_numbers[i:i+25].copy()
        repeats = 0
        for num in temp_list:
            repeats += 1
            value = list_of_numbers[i+25] - num
            if value in temp_list and value != num:
                break
            else:
                continue
        if repeats == len(temp_list):
            return print(f"Here is mistake {list_of_numbers[i+25]}")


def looking_for_answer(list_of_numbers, value):
    index = list_of_numbers.index(value)
    beg = 0
    for i in range(len(list_of_numbers)):
        temp_list = list_of_numbers[beg:index].copy()
        sum_of_num = []
        for n in temp_list:
            sum_of_num.append(n)
            if sum(sum_of_num) == value:
                return print("Encryption key is:", min(sum_of_num) + max(sum_of_num))
                beg = -1
                exit()
            elif sum(sum_of_num) < value:
                continue
            else:
                beg += 1
                break


checking_xmas_encryption(list_of_numbers)
looking_for_answer(list_of_numbers, 675280050) #The result from previous function