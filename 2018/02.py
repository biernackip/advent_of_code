import numpy as np
import collections

# load the file
words = np.loadtxt('./input02.txt', dtype=str)

# Part I
# set the counters
twos = 0
threes = 0

# each line is a "word"
for word in words:
    key_vals = collections.Counter(word).values()
    # check if they appear
    if 2 in key_vals:
        twos += 1
    if 3 in key_vals:
        threes += 1

# print the result
print(twos*threes)


# Part II
# test set:
# words = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']

# empty containers
heads = []  # stores before split
tails = []  # stores after split

# we don't want to split at first or last char
for i in range(1, len(words[0])-1):
    for j in range(len(words)):
        heads.append(words[j][:i])
        tails.append(words[j][i+1:])

    # checking
    for k in range(len(heads)):
        for l in range(len(heads)):
            if k != l:
                if heads[k] == heads[l]:
                    if tails[k] == tails[l]:
                        # solution found
                        print(heads[k]+tails[k])
                        break
    # reset
    heads = []
    tails = []
