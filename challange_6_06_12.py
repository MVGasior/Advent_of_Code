#Sixth challange from advent calendar (06.12.2020)
#Author: Matuesz Gąsior
answers_1 = []
group_answers = set()

for line in open('input_06_12').read().split('\n\n'):
    for answer in line:
        if answer != '\n':
            group_answers.add(answer)
    answers_1.append(len(group_answers))
    group_answers = set()

print(sum(answers_1))

num_of_lines = 0
answers_2 = []
answer_counter = {}
for line in open('input_06_12').read().split('\n\n'):
    if line[-1] == '\n':
        lines = line.count('\n')
    else:
        lines = line.count('\n') + 1
    for answer in line:
        if answer in answer_counter.keys() and answer != '\n':
            answer_counter[answer] += 1
        elif answer not in answer_counter.keys() and answer != '\n':
            answer_counter[answer] = 1
    answer_counter = [value for value in answer_counter.values() if value == lines]
    answers_2.append(len(answer_counter))
    answer_counter = {}

print(sum(answers_2))
