def solve(lines):
    rules = {}
    my_ticket = []
    tickets = []

    for i in range(20):
        f, r = lines[i].split(':')
        rules[f] = [list(map(int, x.split('-'))) for x in r.strip().split(' or ')]
        rules[f].append([0] * 20)
    my_ticket = list(map(int, lines[22].strip().split(',')))
    for i in range(25, len(lines)):
        tickets.append(list(map(int, lines[i].strip().split(','))))

    vals = [0] * 1000
    for k, v in rules.items():
        start = v[0][0]
        end = v[0][1]
        vals[start:end] = [1] * (end-start)
        start = v[1][0]
        end = v[1][1]
        vals[start:end] = [1] * (end-start)

    good_ticks = []
    for t in range(len(tickets)):
        valid = True
        for v in range(len(tickets[t])):
            if vals[ tickets[t][v] ] != 1:
                valid = False
        if valid:
            good_ticks.append(tickets[t][:])


    for t in range(len(good_ticks)):
        for i in range(len(good_ticks[t])):
            for k,v in rules.items():
                if (rules[k][2][i] == 0 and
                   (good_ticks[t][i] < v[0][0] or
                   v[0][1] < good_ticks[t][i] < v[1][0] or
                   v[1][1] < good_ticks[t][i])):
                    rules[k][2][i] = -1

    changed = True
    while changed:
        changed = False
        for k, v in rules.items():
            if len([x for x in v[2] if x == 0]) == 1:
                changed = True
                i = v[2].index(0)
                for l in rules.keys():
                    if l == k:
                        rules[l][2][i] = 1
                    else:
                        rules[l][2][i] = -1

    p = 1        
    for k, v, in rules.items():
        if k[0:9] == 'departure':
            p *= my_ticket[v[2].index(1)]
    return p

if __name__ == '__main__':
    lines = []
    with open('16.txt') as f:
        for line in f.readlines():
            lines.append(line)
    print(solve(lines))
