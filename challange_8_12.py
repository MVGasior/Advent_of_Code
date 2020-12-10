# Eighth challange from advent calendar (08.12.2020)
# Author: Matuesz Gąsior
from copy import deepcopy

moves = []
for i in open('input_08_12'):
    moves.append(i.replace('\n', '').split(' '))

moves.append(['end', '0'])


def game_moves(i=0, acc=0, move_range=[], available_moves=moves):
    if i not in move_range:
        move_range.append(i)
        if available_moves[i][0] == 'acc':
            acc += int(available_moves[i][1])
            i += 1
            return game_moves(i, acc, move_range, available_moves)
        elif available_moves[i][0] == 'jmp':
            i += int(available_moves[i][1])
            return game_moves(i, acc, move_range, available_moves)
        elif available_moves[i][0] == 'end':
            return acc, 'win'
        else:
            i += 1
            return game_moves(i, acc, move_range, available_moves)
    else:
        return acc


def improve_game(opt_move=moves):
    moves_2 = deepcopy(opt_move)
    for move in range(len(opt_move)):
        if opt_move[move][0] == 'jmp':
            moves_2[move][0] = 'nop'
            result = game_moves(move_range=[], available_moves=moves_2)
            if type(result) is tuple:
                return f"This is wining point acc is: {result[0]}"
        elif opt_move[move][0] == 'nop' and opt_move[move][1] != '0':
            moves_2[move][0] = 'jmp'
            result = game_moves(move_range=[], available_moves=moves_2)
            if type(result) is tuple:
                f"This is wining point acc is: {result[0]}"
        moves_2 = deepcopy(opt_move)

print(improve_game())