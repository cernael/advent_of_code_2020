def solve(lines):
    cubes = [[list(x.strip()) for x in lines]]

    n = 0
    while n < 6:
        n += 1
        newc = [[['.'  for x in range(len(cubes[0][0]) + 2)]
                       for y in range(len(cubes[0]) + 2)]
                       for z in range(len(cubes) + 2)]

        for z in range(len(newc)):
            for y in range(len(newc[0])):
                for x in range(len(newc[0][0])):
                    neigh = ''.join([cubes[c][b][a]
                                 for a in [x-2, x-1, x]
                                 for b in [y-2, y-1, y]
                                 for c in [z-2, z-1, z]
                                 if (len(cubes[0][0]) > a >= 0
                                 and len(cubes[0]) > b >= 0
                                 and len(cubes) > c >= 0
                                 and (a != x-1 or b != y-1 or c != z-1)
                                 and cubes[c][b][a] == '#'
                            )])
                    if len(neigh) == 3 : 
                        newc[z][y][x] = '#'
                    elif (len(neigh) == 2 and 
                        0<=x-1<len(cubes[0][0]) and
                        0<=y-1<len(cubes[0]) and
                        0<=z-1<len(cubes) and
                        cubes[z-1][y-1][x-1] == '#'
                       ):
                        newc[z][y][x] = '#'
                    else:
                        newc[z][y][x] =='.'

        cubes = newc
    res = 0
    for z in range(len(cubes)):
        for y in range(len(cubes[0])):
                res += ''.join(cubes[z][y]).count('#')
    return res

if __name__ == '__main__':
    lines = []
    with open('17.txt') as f:
        for line in f.readlines():
            lines.append(line)
    print(solve(lines))
