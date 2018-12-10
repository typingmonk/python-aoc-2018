rules   = []
starter = set()
for line in open("input.txt"):
    start = line.strip().replace("\n","").split(" ")[1]
    end   = line.strip().replace("\n","").split(" ")[7]
    rules.append((start,end))

for idx,element in enumerate(rules):
    check = element[0]
    flag = True
    for i in range(len(rules)):
        if rules[i][1] == check:
            flag = False
            break
    if flag:
        starter.add(check)

roads = list(starter)
print(rules)

nxt = list()
new_road_flag = True

while new_road_flag:
    new_road_flag = False
    for check in roads:
        check_flag = True
        for element in rules:
            if check[len(check)-1] == element[0]:
                nxt.append(check+element[1])
                check_flag    = False
                new_road_flag = True
        if check_flag:
            nxt.append(check)
    roads = nxt
    nxt   = list()

roads.sort()
choices = set()
ans = list()
nxt = list()

has_choice = True
while len(roads):
    for road in roads:
        candidate = road[0]
        isPass = True
        for road in roads:
            if len(road) > 1 and candidate in road[1:]:
                isPass = False
                break
        if isPass:
            break
    ans.append(candidate)
    for road in roads:
        if candidate == road[0]:
            road = road[1:]
        if len(road) > 0:
            nxt.append(road)
    roads = nxt
    roads.sort()
    print(roads)
    nxt = list()



print("".join(ans))
    


