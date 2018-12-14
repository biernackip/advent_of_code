with open('input08.txt') as f:
    raw_tree = f.readline()[:-1]

raw_tree = [int(x) for x in raw_tree.split()]


def parse(data):
    children, metas = data[:2]
    data = data[2:]
    scores = []
    totals = 0

    for i in range(children):
        total, score, data = parse(data)
        totals += total
        scores.append(score)

    totals += sum(data[:metas])

    if children == 0:
        return (totals, sum(data[:metas]), data[metas:])
    else:
        return (
            totals,
            sum(scores[k - 1]
                for k in data[:metas] if k > 0 and k <= len(scores)),
            data[metas:]
        )


total, value, remaining = parse(raw_tree)

print('part 1:', total)
print('part 2:', value)
