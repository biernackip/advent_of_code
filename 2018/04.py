import collections
import numpy as np

# input
with open('./input04.txt', 'r') as f:
    guard_log = f.readlines()

guard_log.sort()

guards = collections.defaultdict(list)
times = collections.defaultdict(int)

for line in guard_log:
    time, action = line.split('] ')
    time = time[15:17]

    if 'Guard' in line:
        guard = int(action.split()[1][1:])
    elif 'falls asleep' in line:
        start = int(time)
    elif 'wakes up' in line:
        end = int(time)
        guards[guard].append((start, end))
        times[guard] += (end-start)


(guard, time) = max(times.items(), key=lambda i: i[1])
(minute, count) = max([(minute, sum(1 for start, end in guards[guard]
                                    if start <= minute < end)) for minute in range(60)], key=lambda i: i[1])
print(guard, time, minute)
print('part 1:', guard * minute)

(guard, minute, count) = max([
    (guard, minute, sum(1 for start,
                        end in guards[guard] if start <= minute < end))
    for minute in range(60) for guard in guards], key=lambda i: i[2])

print(guard, time, minute)
print('part 2:', guard * minute)
