from matplotlib import pyplot as plt
import numpy as np

# real setup
n_grid = 300
serial_number = 1955

fuel_grid = np.zeros(n_grid*n_grid).reshape(n_grid, n_grid)


def calc(x, y, serial_number):
    rack_id = x+10
    power = rack_id*y+serial_number
    return int(str(power*rack_id)[-3])-5

# tests
# print(calc(122, 79, 57))  # -5
# print(calc(217, 196, 39))  # 0
# print(calc(101, 153, 71))  # 4


# populate
for i in range(n_grid):
    for j in range(n_grid):
        fuel_grid[i][j] = calc(i+1, j+1, serial_number)
i = 0
j = 0
print(fuel_grid[i:i+3, j:j+3].sum())

stamp_max = 0
best_vals = [0, 0, 0]
# sum sub windows
for k in range(1, n_grid):
    grid_window_sum = np.zeros(n_grid*n_grid).reshape(n_grid, n_grid)
    for i in range(n_grid-k+1):
        for j in range(n_grid-k+1):
            grid_window_sum[i][j] = fuel_grid[i:i+k, j:j+k].sum()
    y = np.argmax(grid_window_sum) % n_grid
    x = int((np.argmax(grid_window_sum)-y)/n_grid)

    # correcting for indexing from zero
    x += 1
    y += 1

    if np.max(grid_window_sum) > stamp_max:
        stamp_max = np.max(grid_window_sum)
        best_vals = [x, y, k]

print(best_vals)
