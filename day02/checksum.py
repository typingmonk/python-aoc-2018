with open("input.txt", "r") as ins:
    inputs = []
    for line in ins:
        inputs.append(line.replace("\n",""))

print(inputs)
counter = [0,0]

for string in inputs:
    charSet = set(string)
    twoFlag = False
    threeFlag = False
    for char in charSet:
        count = 0
        for i in range(len(string)):
            if(char == string[i]):
                count += 1
        if count == 2:
            twoFlag = True
        elif count == 3:
            threeFlag = True
        if (twoFlag and threeFlag):
            break
    if twoFlag:
        counter[0] += 1
    if threeFlag:
        counter[1] += 1

final = counter[0] * counter[1]

print(counter)
print(final)