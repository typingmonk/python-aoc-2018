def getDigit(number):
    string = str(number)
    if len(string) >= 3:
        return int(string[len(string)-3])
    else:
        return 0

def getPL(x,y,grid,s):
    total = 0
    for i in range(s):
        for j in range(s):
                total += grid[y+i][x+j]
    return total

input = 9798
grid  = []
for y in range(300):
    line = []
    for x in range(300):
        rID = x + 10
        line.append(getDigit(rID * (rID * y + input)) - 5)
    grid.append(line)

pLevel_per_size = []
locations       = []
for size in range(2,14,1):
        print("size",size)
        p_levels = []
        for y in range(300 - size):
                for x in range(300 - size):
                        p_levels.append(getPL(x,y,grid,size))
        idx = p_levels.index(max(p_levels))
        X = idx %  (300 - size)
        Y = idx // (300 - size)
        pLevel_per_size.append(max(p_levels))
        locations.append((X,Y))
idx = pLevel_per_size.index(max(pLevel_per_size))
print(idx+2)
print(locations[idx][0],locations[idx][1],idx+2)