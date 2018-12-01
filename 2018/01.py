import numpy as np

# find the sum of all the frequencies (part I)
frequencies = np.loadtxt('./input01.txt', dtype=int)
print(frequencies.sum())

# find (part II)
# test arrays
# frequencies = np.array([7, +7, -2, -7, -4]) # 14
# frequencies = np.array([-6, +3, +8, +5, -6]) # 5

i = 0
freq_sum = 0
hash_length = len(frequencies)**2
pos_hashtable = np.zeros(hash_length)
neg_hashtable = np.zeros(hash_length)

while True:
    freq_sum += frequencies[i % len(frequencies)]
    if freq_sum >= 0:  # positive index
        if pos_hashtable[abs(freq_sum)] == 1:  # collision
            print(freq_sum)
            break
        else:
            pos_hashtable[freq_sum] = 1
    else:  # negative index
        if neg_hashtable[abs(freq_sum)] == 1:  # collision
            print(freq_sum)
            break
        else:
            neg_hashtable[abs(freq_sum)] = 1
    i += 1  # makes sure things are looping around the input
