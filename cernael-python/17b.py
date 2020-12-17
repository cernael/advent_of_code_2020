def solve(lines):
    cubes = [[[list(x.strip()) for x in lines]]]

    n = 0
    while n < 6:
        n += 1
        newc = [[[['.' for x in range(len(cubes[0][0][0]) + 2)]
                       for y in range(len(cubes[0][0]) + 2)]
                       for z in range(len(cubes[0]) + 2)]
                       for w in range(len(cubes) + 2)]

        for w in range(len(newc)):
            for z in range(len(newc[0])):
                for y in range(len(newc[0][0])):
                    for x in range(len(newc[0][0][0])):
                        neigh = ''.join([cubes[d][c][b][a]
                                     for a in [x-2, x-1, x]
                                     for b in [y-2, y-1, y]
                                     for c in [z-2, z-1, z]
                                     for d in [w-2, w-1, w]
                                     if (len(cubes[0][0][0]) > a >= 0
                                     and len(cubes[0][0]) > b >= 0
                                     and len(cubes[0]) > c >= 0
                                     and len(cubes) > d >= 0
                                     and (a != x-1 or b != y-1 or c != z-1 or d != w-1)
                                     and cubes[d][c][b][a] == '#'
                                )])
                        if len(neigh) == 3 : 
                            newc[w][z][y][x] = '#'
                        elif (len(neigh) == 2 and 
                            0<=x-1<len(cubes[0][0][0]) and
                            0<=y-1<len(cubes[0][0]) and
                            0<=z-1<len(cubes[0]) and
                            0<=w-1<len(cubes) and
                            cubes[w-1][z-1][y-1][x-1] == '#'
                           ):
                            newc[w][z][y][x] = '#'
                        else:
                            newc[w][z][y][x] =='.'

        cubes = newc
    res = 0
    for w in range(len(cubes)):
        for z in range(len(cubes[0])):
            for y in range(len(cubes[0][0])):
                res += ''.join(cubes[w][z][y]).count('#')
    return res

if __name__ == '__main__':
    lines = []
    with open('17.txt') as f:
        for line in f.readlines():
            lines.append(line)
    print(solve(lines))
