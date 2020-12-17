def solve(lines):
    rules = {}
    my_ticket = []
    tickets = []

    for i in range(20):
        f, r = lines[i].split(':')
        rules[f] = [list(map(int, x.split('-'))) for x in r.strip().split(' or ')]
    my_ticket = list(map(int, lines[22].strip().split(',')))
    for i in range(25, len(lines)):
        tickets.append(list(map(int, lines[i].strip().split(','))))

    vals = [0] * 1000
    for k, v in rules.items():
        start = v[0][0]
        end = v[0][1]+1
        vals[start:end] = [1] * (end-start)
        start = v[1][0]
        end = v[1][1]+1
        vals[start:end] = [1] * (end-start)

    tser = 0
    for t in range(len(tickets)):
        for v in range(len(tickets[t])):
            if vals[ tickets[t][v] ] != 1:
                tser += tickets[t][v]
            
    return tser

if __name__ == '__main__':
    lines = []
    with open('16.txt') as f:
        for line in f.readlines():
            lines.append(line)
    print(solve(lines))
