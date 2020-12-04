#Third challange from advent calendar (03.12.2020)
#Author: Matuesz Gąsior

count = 0
with open("input_03_12") as file:
    i = 0
    j = 0
    word_list = []
    for word in file:
        if word[i] == '#' and j % 2 == 0:
            count += 1
        if i >= 30:
            i = i - 30
        else:
            i += 1
        j += 1

#word_list = [word_list[i] for i in range(len(word_list)) if i % 2 == 0]
#for words in word_list:
    '''
    if word[i] == '#':
        count += 1
    if i >= 28:
        i = i - 28
    else:
        i += 3
    '''
print(count)
