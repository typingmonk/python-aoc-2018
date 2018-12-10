positions = []
velocitys = []
densitys  = []

def dist(x_center,y_center,position):
    ans  = (position[0] - x_center) ** 2
    ans += (position[1] - y_center) ** 2
    ans  = ans ** (0.5)
    return ans

for line in open("input.txt"):
    line = line.strip().replace("<","")
    line = line.replace(">","")
    line = line.replace("=","")
    line = line.replace("velocity",",")
    line = line.replace("position","")
    line = line.replace(" ","")
    line = list(map(int,line.split(",")))
    positions.append(line[0:2])
    velocitys.append(line[2:4])

for i in range(25000):
    ## calcuate the density of stars
    print(i)
    density = 0
    x_center = sum([ position[0] for position in positions ]) / len(positions)
    y_center = sum([ position[1] for position in positions ]) / len(positions)
    for position in positions:
        if dist(x_center,y_center,position) != 0:
            density += 1 / dist(x_center,y_center,position)
        else:
            print("divide by zero when : ",i)
    densitys.append(density)
    if i == 10312:
    ##if i == 3:
        break
    ## calculate next second
    for idx,position in enumerate(positions):
        position[0] += velocitys[idx][0]
        position[1] += velocitys[idx][1]


##print(positions)
minX = min([ position[0] for position in positions ])
maxX = max([ position[0] for position in positions ])
minY = min([ position[1] for position in positions ])
maxY = max([ position[1] for position in positions ])
## transformantion
for position in positions:
    position[0] -= minX
    position[1] -= minY
## print the sky 
f = open("output.txt","w")
for j in range(maxY-minY+1):
    aLine = ["." for k in range(maxX-minX+1)]
    for i in range(maxX-minX+1):
        for position in positions:
            if [i,j] == position:
                aLine[i] = "*"
    f.write("".join(aLine) + "\n")
f.close()

##print(densitys)
print(densitys.index(max(densitys)))