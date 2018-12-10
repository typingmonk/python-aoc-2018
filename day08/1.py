for line in open("input.txt"):
    data = list(map(int,line.split(" ")))
answer = 0

one_left = False
while not one_left:
    for i in range(0,len(data),2):
        if data[i] == 0:
            if i > 0:
                idx_parent = i - 2
                idx_node   = i
                break
            elif i == 0:
                one_left = True
    if one_left:
        for i in range(2,len(data)):
            answer += data[i]
    else:
        metadata_count = data[idx_node+1]
        for i in range(metadata_count):
            answer += data[idx_node+2]
            data.pop(idx_node+2)
        data.pop(idx_node+1)
        data.pop(idx_node)
        data[idx_parent] -= 1

print(answer)