for line in open("input.txt"):
    data = list(map(int,line.split(" ")))
answer = 0
##print(data)
one_left = False
while not one_left:
    forward = 0
    for i in range(0,len(data),2):
        forward_i = i + forward - forward * 2
        """
        print("=================")
        print("forward         : ",forward)
        print("i               : ",i)
        print("data[forward_i] : ",data[forward_i])
        """
        if data[forward_i] == 0:
            if forward_i > 0:
                idx_node   = forward_i
                idx_parent = forward_i
                while True:
                    if type(data[idx_parent-1]) is str:
                        idx_parent -= 1
                    else:
                        break
                idx_parent -= 2
            elif forward_i == 0:
                one_left = True
            break
        if type(data[forward_i]) is str:
            forward += 1
    if one_left:
        values = list()
        while True:
            if type(data[2]) is str:
                values.append(int(data[2][1:]))
                data.pop(2)
            else:
                break
        for i in range(data[1]):
            if data[2+i]-1 in range(len(values)):
                answer += values[data[2+i]-1]
    else:
        metadata_count = data[idx_node+1]
        isStr = True
        values = list()
        """
        checkList = []
        for j in range(-3,10):
            checkList.append(data[idx_node+j])
        print("checkList : ",checkList)
        """
        while True:
            if type(data[idx_node+2]) is str:
                values.append(int(data[idx_node+2][1:]))
                data.pop(idx_node+2)
            else :
                break
        node_value = 0
        for i in range(metadata_count):
            if len(values) > 0:
                """
                checkList = []
                for j in range(-3,6):
                    checkList.append(data[idx_node+j])
                print("checkList : ",checkList)
                """
                if data[idx_node+2]-1 in range(len(values)):
                    node_value += values[data[idx_node+2]-1]
            elif len(values) == 0:
                node_value += data[idx_node+2]
            if i == metadata_count-1:
                data[idx_node+2] = "v" + str(node_value)
            else:
                data.pop(idx_node+2)
        data.pop(idx_node+1)
        data.pop(idx_node)
        data[idx_parent] -= 1
        ##print(data)
print(answer)