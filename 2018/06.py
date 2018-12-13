import numpy as np
from matplotlib import pyplot as plt

# test input
# xs, ys = np.loadtxt('./test_input06.txt', dtype=int, delimiter=',').T
# map_size = 10

xs, ys = np.loadtxt('./input06.txt', dtype=int, delimiter=',').T
map_size = 400

# Part I

if False:

    edge_points = []
    world_map = np.zeros(map_size*map_size).reshape(map_size, map_size)
    dist_map = np.ones(map_size*map_size).reshape(map_size, map_size)*map_size

    for i in range(map_size):
        for j in range(map_size):
            for k in range(len(xs)):
                # calculate the distance between
                # xs[k],ys[k] and i,j
                dist = abs(i-xs[k])+abs(j-ys[k])
                # if conflict, mark as negative index of a point
                if dist == dist_map[i][j]:
                    world_map[i][j] = -1
                # if distance smaller than present, assign to different point
                if dist < dist_map[i][j]:
                    dist_map[i][j] = dist
                    world_map[i][j] = k
                    # take edges as points with infinite area
                    if i == 0 or j == 0 or i == map_size-1 or j == map_size-1:
                        edge_points.append(k)

    # just nasty looking way to get edge points as a list
    edge_points = set(list(np.array([list(world_map[0]), list(
        world_map[-1]), list(world_map.T[0]), list(world_map.T[-1])], dtype=int).flatten()))

    largest_area = 0
    for k in range(len(xs)):
        if k not in set(edge_points):
            k_area = len(world_map[np.where(world_map == k)])
            if k_area > largest_area:
                largest_area = k_area

    print(largest_area)

    # here comes some viz
    plt.scatter(xs, ys, c='r')
    # different color for edge points
    for l in list(edge_points):
        plt.scatter(xs[l], ys[l], c='cyan')
    plt.savefig('./06_points.pdf')

    plt.imshow(dist_map.T)
    plt.savefig('06_dist.pdf')
    plt.imshow(world_map.T)
    plt.savefig('06_assignment.pdf')

# Part II
total_distance_map = np.zeros(map_size*map_size).reshape(map_size, map_size)
for i in range(map_size):
    print(i)
    for j in range(map_size):
        for k in range(len(xs)):
            total_distance_map[i][j] += abs(i-xs[k])+abs(j-ys[k])
            if total_distance_map[i][j] > 10002:
                break

# print(total_distance_map[np.where(total_distance_map<32)].size) # test case
print(total_distance_map[np.where(total_distance_map < 10000)].size)

# here comes some viz
plt.scatter(xs, ys, c='r')
plt.imshow(total_distance_map.T)
plt.savefig('06_total_distance.pdf')
