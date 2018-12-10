import math

pins      = []
pin_count = []
border = set()

## shitty variables init
minX = 99999
minY = 99999
maxX = 0
maxY = 0

## calcuate Manhattan distance  
## for given (x,y) to each coordinates
## pin_count records numbers of determined coordinate ocurred
def decideLabel(x,y):
    pin_dist = []
    for idx, pin in enumerate(pins):
        taxiDist = abs(pin[0] - x) + abs(pin[1]-y)
        pin_dist.append(taxiDist)
    min_dist = min(pin_dist)
    if pin_dist.count(min_dist) == 1:
        pin_count[pin_dist.index(min_dist)] += 1
    return pin_dist.index(min_dist)


for line in open("input.txt"):
    line = line.strip().replace(" ","")
    pin_count.append(0)
    X = int(line.split(",")[0])
    Y = int(line.split(",")[1])
    pins.append((X,Y))
    if minX > X:
        minX = X
    if minY > Y:
        minY = Y
    if maxX < X:
        maxX = X
    if maxY < Y:
        maxY = Y

## decide center grid and raduis(In Manhattan distance aspect)
mid_pin = math.floor((maxX - minX) / 2), math.floor((maxY - minY) / 2)
radius = max(maxX - minX,maxY - minY)

## iterate all grids inside given center and raduis
for i in range(radius):
    for dist in range(-i,i+1):
        x = mid_pin[0] + dist
        y = mid_pin[1] + (i - abs(dist))
        decideLabel(x,y)
        if (i - abs(dist)) == 0:
            continue
        y = mid_pin[1] - (i - abs(dist))
        decideLabel(x,y)

## collect coordinates ocurred on the very edge
## seeing those coordinates as having infinite areas
## then rule out those coordinates
for dist in range(-radius,radius+1):
    x = mid_pin[0] + dist
    y = mid_pin[1] + (i - abs(dist))
    border.add(decideLabel(x,y))
    y = mid_pin[1] - (i - abs(dist))
    border.add(decideLabel(x,y))

for idx in border:
    pin_count[idx] = 0

print(max(pin_count))