rules   = []
starter = set()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def duration(letter):
    return 60 + alphabet.index(letter) + 1

number_of_workers = 5
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
print(roads)

shift_system = list()
for i in range(number_of_workers):
    shift_system.append({"task":"","time":0})

timer = 0
while(len(roads)>0):
    timer         += 1
    collectTasks   = list()
    tasks          = set()
    finished_tasks = set()
    nxt_roads      = list()
    for road in roads:
        aTask = road[0]
        isPass = True
        for road in roads:
            if aTask in road[1:]:
                isPass = False
        if isPass:
            collectTasks.append(aTask)
    collectTasks.sort()
    for task in collectTasks:
        tasks.add(task)
    for task in tasks:
        task_is_processing = False
        for worker in shift_system:
            if worker["task"] == task:
                task_is_processing = True
                break
        if not task_is_processing:
            for worker in shift_system:
                if worker["task"] == "":
                    worker["task"] = task
                    task_is_processing = True
                    break                
    print("shift_system : ",shift_system)
    for worker in shift_system:
        if worker["task"] != "":
            if worker["time"] + 1 == duration(worker["task"]):
                finished_tasks.add(worker["task"])
                worker["task"] = ""
                worker["time"] = 0
            else:
                worker["time"] += 1
    for finished_task in finished_tasks:
        for road in roads:
            if road[0] == finished_task and len(road) > 1:
                nxt_roads.append(road[1:])
            elif road[0] != finished_task:
                nxt_roads.append(road)
    if len(finished_tasks) == 0:
        nxt_roads = roads
    roads = nxt_roads
    ##print("len(roads) : ",len(roads))
    ##print("====================")
print("timer  : ",timer)