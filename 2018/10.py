from matplotlib import pyplot as plt
import numpy as np

x = []
y = []
vx = []
vy = []

with open('input10.txt') as f:
    # with open('test_input10.txt') as f:
    lines = f.readlines()


# split lines
for line in lines:
    x.append(int(line.split(',')[0].split('<')[-1]))
    y.append(int(line.split(',')[1].split('>')[0]))
    vx.append(int(line.split('velocity=<')[1].split(',')[0]))
    vy.append(int(line.split('velocity=<')[1].split(',')[1].split('>')[0]))

# turn into numpy arrays
x = np.array(x)
y = np.array(y)
vx = np.array(vx)
vy = np.array(vy)

# let's minimize distance
maxx = 10000
best_t = 0

for t in range(10300, 10500):
    xt = x+t*vx
    yt = y+t*vy

    if max(xt)-min(xt) < maxx:
        maxx = max(xt)-min(xt)
        best_t = t

# viz
plt.scatter(x+best_t*vx, y+best_t*vy, s=3)
plt.savefig('viz_10.pdf')
print(best_t)
