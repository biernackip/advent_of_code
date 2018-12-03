import numpy as np

viz = False
# test input
patches = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']

# input
with open('./input03.txt', 'r') as f:
    patches = f.readlines()

# Part I
# setting up the fabric
fabric = np.zeros(1000*1000).reshape(1000, 1000)

# scanning the patches
for patch in patches:
    x_corner = int(patch.split(' ')[2].split(',')[0])
    y_corner = int(patch.split(' ')[2].split(',')[1].split(':')[0])
    x_len = int(patch.split(' ')[3].split('x')[0])
    y_len = int(patch.split(' ')[3].split('x')[1])

    for i in range(x_len):
        for j in range(y_len):
            fabric[i+x_corner][j+y_corner] += 1

# answer to Part I:
print(len(fabric[np.where(fabric > 1)]))

if viz:
    # vizualisation of the claimed fabric:
    from matplotlib import pyplot as plt
    plt.imshow(fabric)
    plt.savefig('03.pdf')

# Part II
for patch in patches:
    x_corner = int(patch.split(' ')[2].split(',')[0])
    y_corner = int(patch.split(' ')[2].split(',')[1].split(':')[0])
    x_len = int(patch.split(' ')[3].split('x')[0])
    y_len = int(patch.split(' ')[3].split('x')[1])

    stamp_size = x_len*y_len  # target
    stamp_count = 0  # counter
    for i in range(x_len):
        for j in range(y_len):
            stamp_count += fabric[i+x_corner][j+y_corner]
    # if there is no overlap, then only sum of singles will
    if stamp_count == stamp_size:
        # answer to Part II:
        print(patch)
