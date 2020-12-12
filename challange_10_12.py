# Tenth challange from advent calendar (10.12.2020)
# Author: Matuesz Gąsior

list_of_adapters = []
for line in open('input_10_12'):
    list_of_adapters.append(int(line.replace('\n', '')))

list_of_adapters.sort()
list_of_adapters.append(max(list_of_adapters) + 3)


def ones_threes(list_of):
    output = 0
    ones = 0
    twos = 0
    threes = 0
    for adapt in list_of:
        diff = adapt - output
        if diff == 1:
            ones += 1
        elif diff == 2:
            twos += 1
        elif diff == 3:
            threes += 1
        else:
            print("problem!")
        output = adapt
    return ones * threes


num_ways = 0


def possible_ways(list_of, num_ways=0):
    for i in range(len(list_of)-1):
        if i != 0:
            diff = (list_of[i] - list_of[i - 1]) + (list_of[i + 1] - list_of[i])
            if diff <= 3:
                var = list_of.copy()
                var.pop(i)
                num_ways = possible_ways(var, num_ways)
                num_ways += 1
            else:
                continue
        else:
            continue
    print(num_ways)
    return num_ways


print(possible_ways(list_of_adapters))

ones_threes(list_of_adapters)
