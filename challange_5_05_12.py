#Fivth challange from advent calendar (05.12.2020)
#Author: Matuesz Gąsior
seat_id = []
for boarding_code in open('input_05_12').read().split('\n'):
    row = '0b0' + boarding_code[:7].replace('F', '0').replace('B', '1')
    column = '0b0' + boarding_code[7:].replace('R', '1').replace('L', '0')
    seat_id.append(int(row, 2) * 8 + int(column, 2))

print(max(seat_id))

for i in range(865):
    if i not in seat_id and 74 < i < 865:
        print(i)
    else:
        continue

