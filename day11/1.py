def getDigit(number):
    string = str(number)
    if len(string) >= 3:
        return int(string[len(string)-3])
    else:
        return 0

def getPL(x,y,grid):
    total = 0
    for i in range(3):
        for j in range(3):
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

p_levels = []
for y in range(298):
    for x in range(298):
        p_levels.append(getPL(x,y,grid))


idx = p_levels.index(max(p_levels))
X = idx %  298
Y = idx // 298
print(idx)
print(X,Y)