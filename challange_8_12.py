#Eighth challange from advent calendar (06.12.2020)
#Author: Matuesz Gąsior


moves = []
for i in open('input_08_12'):
    moves.append(i.replace('\n', '').split(' '))
moves.append('end')


def game_moves(i=0, acc=0, move_range=[], available_moves=moves):
    if i not in move_range:
        move_range.append(i)
        if available_moves[i][0] == 'acc':
            acc += int(available_moves[i][1])
            i += 1
        elif available_moves[i][0] == 'jmp':
            i += int(available_moves[i][1])
        elif available_moves[i][0] == 'end':
            return f'end game acc is: {acc}'
        else:
            i += 1
        game_moves(i, acc, move_range)
    else:
        return 888

#in progress
'''
def game_improve(available_moves=moves):
    for move in range(len(available_moves)):
        working_spaces = available_moves.copy()
        if available_moves[move][0] == 'jmp':
            working_spaces[move][0] = 'nop'
            print(working_spaces)
            result = game_moves(available_moves=working_spaces)
            if result is str:
                return result
            else:
                continue
        elif available_moves[move][0] == 'nop' and available_moves[move][1] != '0':
            working_spaces[move][0] = 'jmp'
            print(working_spaces)
            result = game_moves(available_moves=working_spaces)
            if result is str:
                return result
            else:
                continue

'''

game_improve()
print(game_improve())
