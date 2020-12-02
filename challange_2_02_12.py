#Second challange from advent calendar (02.12.2020)
#Author: Matuesz Gąsior

password_list = []
num = 0
new_num = 0
with open("input_02_12") as file:
    for word in file:
        password_list.append(word[:-1])
for line in password_list:
    password = line.split(' ')
    count = password[0].split('-')
    if int(count[0]) <= password[2].count(password[1][0]) <= int(count[1]):
        num += 1
    if (password[2][int(count[0]) - 1] == password[1][0] and password[2][int(count[1]) - 1] != password[1][0]) or \
            (password[2][int(count[1]) - 1] == password[1][0] and password[2][int(count[0]) - 1] != password[1][0]):
        new_num += 1
print(num)
print(new_num)


