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

for i in range(14000):
    ## calcuate the density of stars
    ##print(i)
    density = 0
    x_center = sum([ position[0] for position in positions ]) / len(positions)
    y_center = sum([ position[1] for position in positions ]) / len(positions)
    for position in positions:
        if dist(x_center,y_center,position) != 0:
            density += 1 / dist(x_center,y_center,position)
        else:
            print("divide by zero when : ",i)
    densitys.append(density)
    
    ## calculate next second
    for idx,position in enumerate(positions):
        position[0] += velocitys[idx][0]
        position[1] += velocitys[idx][1]

print(max(densitys))
print(densitys.index(max(densitys)))