# with open('test_input07.txt') as f:
with open('input07.txt') as f:
    lines = f.readlines()

prereq = []
instr = []
conditions = []
candidates = []
completed = ''

# parse input
for line in lines:
    prereq.append(line.split()[1])
    instr.append(line.split()[-3])

# Part I

letters = list(set().union(instr, prereq))

for letter in letters:
    letter_prereq = []
    for i in range(len(lines)):
        if instr[i] == letter:
            letter_prereq.append(prereq[i])

    conditions.append(letter_prereq)

    # 1. find letters that have no prereq
    if len(letter_prereq) == 0:
        candidates.append(letter)


while len(candidates):
    # 2. sort candidates and take first as starting
    completed += sorted(candidates)[0]
    # 3. remove that latter from candidates
    candidates.remove(completed[-1])

    # 4. find letters that got unlocked
    for i in range(len(letters)):
        if letters[i] not in completed:
            # 5. check if all conditions have been completed
            if set(conditions[i]).issubset(set(completed)):
                candidates.append(letters[i])

    # 6. remove repeated letters
    candidates = list(set(candidates))

print('order', completed)

# Part II
import string

conditions = []
candidates = []
time = 0
completed = ''


n_workers = 2
t_extra = 0

n_workers = 5
t_extra = 60

def letter_cost(letter, t_extra):
    return string.ascii_uppercase.rindex(letter)+1+t_extra

workers_free_in = [0 for n in range(n_workers)]
workers_current_letter = ['' for n in range(n_workers)]

letters = list(set().union(instr, prereq))

for letter in letters:
    letter_prereq = []
    for i in range(len(lines)):
        if instr[i] == letter:
            letter_prereq.append(prereq[i])

    conditions.append(letter_prereq)

    # 1. find letters that have no prereq
    if len(letter_prereq) == 0:
        candidates.append(letter)


while len(completed) < len(letters):
    print(time, workers_free_in, workers_current_letter, candidates, completed)
    for w in range(n_workers):

        if workers_free_in[w] == 0 and workers_current_letter[w] != '':
            completed += workers_current_letter[w]

            # 4. find letters that got unlocked
            for i in range(len(letters)):
                if letters[i] not in completed:
                    # 5. check if all conditions have been completed
                    if set(conditions[i]).issubset(set(completed)):
                        candidates.append(letters[i])

            # 6. remove repeated letters
            candidates = list(set(candidates))

            workers_current_letter[w] = ''

        for candidate in candidates:
            if candidate in workers_current_letter or candidate in completed:
                candidates.remove(candidate)

        if workers_current_letter[w] == '' and len(candidates) > 0:
            candidate = sorted(candidates)[0]
            if candidate not in workers_current_letter:
                workers_current_letter[w] = sorted(candidates)[0]
                workers_free_in[w] = letter_cost(workers_current_letter[w], t_extra)

        if workers_free_in[w] > 0:
            workers_free_in[w] -= 1


    time += 1

print('order', completed)
print(time)
