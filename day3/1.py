dimension_map = set()
overlap_points = set()

overlap_claims = set()
claims = set(range(1,1412))

for line in open('input.txt'):
    line = line.strip()
    ##print(line)
    x_y = line.split('@')[1].split(':')[0].strip()
    x = int(x_y.split(',')[0])
    y = int(x_y.split(',')[1])
    a_b = line.split('@')[1].split(':')[1].strip()
    a = int(a_b.split('x')[0])
    b = int(a_b.split('x')[1])

    for i in range(x,x+a):
        for j in range(y,y+b):
            point = str(i)+","+str(j)
            ##print(str(i)+","+str(j))
            if point in dimension_map:
                overlap_points.add(point)
            dimension_map.add(point)

print(len(overlap_points))

for line in open('input.txt'):
    line = line.strip()
    ##print(line)
    claim = x_y = line.split('@')[0]
    x_y = line.split('@')[1].split(':')[0].strip()
    x = int(x_y.split(',')[0])
    y = int(x_y.split(',')[1])
    a_b = line.split('@')[1].split(':')[1].strip()
    a = int(a_b.split('x')[0])
    b = int(a_b.split('x')[1])
    
    for i in range(x,x+a):
        for j in range(y,y+b):
            point = str(i)+","+str(j)
            if point in overlap_points:
                overlap_claims.add(int(str(claim[1:]).strip()))
    
print(claims - overlap_claims)