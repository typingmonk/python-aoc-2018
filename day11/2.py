input = 9798
grid     = []
sa_table = []

def pLevel(x,y,input):
    rID   = x + 10
    power = (y * rID + input) * rID
    power = ((power // 100) % 10 ) - 5
    return power

def sum_area(x,y,grid,sa_table):
    ## s(x,y) = s(x-1,y) + s(x,y-1) - s(x-1,y-1) + p(x,y)
    ## s(x,y) =    A     +    B     -     C      + D
    A = 0 if x-1 < 0 else sa_table[y][x-1]
    B = 0 if y-1 < 0 else sa_table[y-1][x]
    C = 0 if x-1 < 0 or y-1 < 0 else sa_table[y-1][x-1]
    D = grid[y][x]
    return A + B - C + D

def sum_area_by_size(x,y,s,sa_table):
    ## s(x,y) = s(x+s-1,y+s-1) - ( s(x+s-1,y-1) + s(x-1,y+s-1) - s(x-1,y-1))
    ## s(x,y) = s(x+s-1,y+s-1) + s(x-1,y-1) - s(x+s-1,y-1) - s(x-1,y+s-1)
    ## s(x,y) =       A        +      B     -      C       -       D
    A = sa_table[y+s-1][x+s-1]
    B = 0 if x-1 < 0 or y-1 < 0 else sa_table[y-1][x-1]
    C = 0 if y-1 < 0 else sa_table[y-1][x+s-1]
    D = 0 if x-1 < 0 else sa_table[y+s-1][x-1]
    return A + B - C - D

for y in range(300):
    line = []
    for x in range(300):
        line.append(pLevel(x,y,input))
    grid.append(line)

for y in range(300):
    line = []
    for x in range(300):
        line.append(0)
    sa_table.append(line)

for y in range(300):
    for x in range(300):
        sa_table[y][x] = sum_area(x,y,grid,sa_table)

locations = []
pLevels   = []
for size in range(2,301):
    candidates = []
    for y in range(301-size):
        for x in range(301-size):
            candidates.append(sum_area_by_size(x,y,size,sa_table))
    idx = candidates.index(max(candidates))
    X   = idx  %  (301-size)
    Y   = idx  // (301-size)
    pLevels.append(candidates[idx])
    locations.append((X,Y))

idx      = pLevels.index(max(pLevels))
size     = idx + 2
location = locations[idx]
print(location[0],location[1],size)