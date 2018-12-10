import string,math

pins      = []
##pins_name = list("abcdef")
##pin_count = [0 for i in range(6)]
pins_name = string.ascii_lowercase + string.ascii_uppercase[:24]
pin_count = [0 for i in range(50)]
border = set()

target_dist = 10000
count = 0
minX = 99999
minY = 99999
maxX = 0
maxY = 0

def decideLabel(x,y):
    global count
    pin_dist = []
    for idx, pin in enumerate(pins):
        taxiDist = abs(pin[0] - x) + abs(pin[1]-y)
        pin_dist.append(taxiDist)
    total_dist = sum(pin_dist)
    if total_dist < target_dist:
        count += 1
    """
    if pin_dist.count(min_dist) == 1:
        pin_count[pin_dist.index(min_dist)] += 1
    return pin_dist.index(min_dist)
    """


for line in open("input.txt"):
    line = line.strip().replace(" ","")
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

mid_pin = math.floor((maxX - minX) / 2), math.floor((maxY - minY) / 2)
radius = max(maxX - minX,maxY - minY)

for i in range(radius):
    for dist in range(-i,i+1):
        x = mid_pin[0] + dist
        y = mid_pin[1] + (i - abs(dist))
        decideLabel(x,y)
        if (i - abs(dist)) == 0:
            continue
        y = mid_pin[1] - (i - abs(dist))
        decideLabel(x,y)

"""
for dist in range(-radius,radius+1):
    x = mid_pin[0] + dist
    y = mid_pin[1] + (i - abs(dist))
    border.add(decideLabel(x,y))
    y = mid_pin[1] - (i - abs(dist))
    border.add(decideLabel(x,y))

for idx in border:
    pin_count[idx] = 0
"""

print(count)