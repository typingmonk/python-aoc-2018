with open("test.txt", "r") as ins:
    inputs = []
    for line in ins:
        inputs.append(line)

total = 0
record = [0]
twice = []
flag = True

while flag:
        for line in inputs:
            if(line[0:1] == "+"):
                total += int(line[1:])
            else:
                total += -int(line[1:])

            print(total)
    
            if total in record:
                twice.append(total)
                flag = False
                break
            else:
                record.append(total)

print(total)
print(twice)