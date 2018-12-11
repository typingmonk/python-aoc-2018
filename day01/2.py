change_freq = []
for line in open("input.txt"):
    change_freq.append(int(line.strip()))

current = 0
record  = {0}

flag = True
while flag:
    for change in change_freq:
        current += change
        if current in record:
            flag = False
            break
        else:
            record.add(current)

print(current)