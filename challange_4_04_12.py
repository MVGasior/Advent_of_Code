#Fourth challange from advent calendar (04.12.2020)
keys = []
symbols = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
counter = 0
j = 0
with open("input_04_12", 'r') as file:
    for word in file:
        if word == '\n':
            for sym in symbols:
                if sym in keys:
                    j += 1
            if j == 7:
                counter += 1
            j = 0
            keys = []
        else:
            for para in word.split(' '):
                key = para.split(':')[0]
                value = para.split(':')[1].replace(' ', '').replace('\n', '')
                if key == 'byr' and 1920 <= int(value) <= 2002:
                    keys.append(key)
                elif key == 'iyr' and 2010 <= int(value) <= 2020:
                    keys.append(key)
                elif key == 'eyr' and 2020 <= int(value) <= 2030:
                    keys.append(key)
                elif key == 'hgt' and ((value[-2:] == 'in' and 59 <= int(value[:-2]) <= 76) or
                                       (value[-2:] == 'cm' and 150 <= int(value[:-2]) <= 193)):
                    keys.append(key)
                elif key == 'hcl' and value[0] == '#' and len(value) == 7 and value[1:].isalnum():
                    keys.append(key)
                elif key == 'ecl' and (value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) and len(value) == 3:
                    keys.append(key)
                elif key == 'pid' and len(value) == 9:
                    keys.append(key)
                else:
                    continue
print(counter)

