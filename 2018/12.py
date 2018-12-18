import numpy as np

iterations = 20
iterations = 200

# reading input
with open('input12.txt') as f:
    init_state = f.readline().split()[-1]
    f.readline()

    rules = f.readlines()
# interpret rules
for i in range(len(rules)):
    rules[i] = rules[i][:-1].split(' => ')

# full storage
state_tot_length = 4*iterations+len(init_state)

# translate to binary states
init_state_binary = np.zeros(state_tot_length)
for j in range(2*iterations, state_tot_length-2*iterations):
    if init_state[j-2*iterations] == "#":
        init_state_binary[j] = 1

rules_binary = np.zeros(
    len(rules)*len(rules[0][0])).reshape(len(rules), len(rules[0][0]))
switch_binary = np.zeros(len(rules))

for j in range(len(rules)):
    if rules[j][1] == '#':
        switch_binary[j] = 1
    for k in range(len(rules[j][0])):
        if rules[j][0][k] == "#":
            rules_binary[j][k] = 1


# evolving
for i in range(iterations):
    new_state_binary = np.copy(init_state_binary)
    for j in range(len(init_state_binary)-4):
        for k in range(len(rules)):
            if np.array_equal(init_state_binary[j:j+5], rules_binary[k]):
                new_state_binary[j+2] = switch_binary[k]
    init_state_binary = np.copy(new_state_binary)

# multiply the plant by the pot number and sum
    for j in range(state_tot_length):
        new_state_binary[j] *= (j-2*iterations)
    print(i, new_state_binary.sum())
