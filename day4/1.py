def OnOff(startTime,endTime,countTable):
    if (startTime[0:2] == "00") or ( startTime[0:2] == "23" and endTime[0:2] == "23" ):
        for i in range(int(startTime[3:5]),int(endTime[3:5])):
            countTable[i] += 1
    elif startTime[0:2] == "23" and endTime[0:2] == "00":
        for i in range(0,int(endTime[3:5])):
            countTable[i] += 1
        for i in range(int(startTime[3:5]),60):
            countTable[i] += 1
    print("countTable : " + str(countTable) + "\n")
    return countTable

data = []
trackID = "none"
trackFlag = False
startTime = "none"
endTime = "none"
timeArray = []
idArray = []

for line in open('sorted.txt'):
    ##print(line.strip())
    
    ## Record startTime and endTime
    if (("wakes up" in line or "Guard" in line) and trackFlag == True):
        endTime = line[12:17]
        print("endTime : ",line.strip())
        ##print("startTime : "+startTime)
        ##print("endTime : " + endTime)
        ##print("minuteDiff : " + minuteDiff(startTime,endTime))
        print("Worker ID : " + trackID)
        
        if (idArray == []) or (int(trackID) not in idArray):
            idArray.append(int(trackID))
            timeArray.append(OnOff(startTime,endTime,[0 for i in range(60)]))
        
        elif int(trackID) in idArray:
            countTable = timeArray[idArray.index(int(trackID))]
            timeArray[idArray.index(int(trackID))] = OnOff(startTime,endTime,countTable)

    if ("falls asleep" in line and trackFlag == False):
        print("startTime : ",line.strip())
        startTime = line[12:17]

    ## Record worker ID
    if ("Guard" in line):
        trackID = (((line.split("#"))[1]).split(" "))[0]

    ## Record Step
    if (("wakes up" in line ) or ("Guard" in line)):
        trackFlag = False
    if ("falls asleep" in line):
        trackFlag = True
    ##print("============================")

ansID = "none"
maxMin = 0
for i in range(len(idArray)):
    print("id : ",idArray[i])
    print("maxMin : ",timeArray[i])
    print("===================")
    if maxMin < max(timeArray[i]):
        maxMin = max(timeArray[i])
        ansID = idArray[i]
        print(ansID)


## index of timeArray
arrayIndex = idArray.index(ansID)
## max value in timeArray
theMax = max(timeArray[arrayIndex])
## index of timeArray where max value happened
freqMin = timeArray[arrayIndex].index(theMax)

print("FinalID : ",ansID)
print("freqMin : ",freqMin )

print("==========================")
print("Final Ans : ",int(ansID) * int(freqMin))

## sorting rows
"""
data = []
for line in open('input.txt'):
    data.append(line.strip())
data.sort()

sortedFile = open('sorted.txt','a')
for line in data:
    sortedFile.write(line+"\n")
"""