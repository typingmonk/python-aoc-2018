import string
alphabat = string.ascii_lowercase

with open("input.txt") as exampleFile:
    example = exampleFile.readline()

minLen = 20000
for char in alphabat:
    ##print("now doing char : ",char)
    reducedExample = list(example.replace(char,"").replace(char.upper(),""))
    index = 0
    while index < len(reducedExample)-1:
        ##print("=====================")
        ##print("index        : ",index)
        ##print("len(example) : ",len(reducedExample))
        poly1 = reducedExample[index]
        poly2 = reducedExample[index+1]
        ##print("poly1        : ",poly1)
        ##print("poly2        : ",poly2)
        if (poly1.upper() == poly2 and poly1 == poly2.lower()) or (poly1.lower() == poly2 and poly1 == poly2.upper()):
            del reducedExample[index:index+2]
            if index > 0:
                index -= 1
        else:
            index += 1
    ##print("left len : ",len(reducedExample))
    if len(reducedExample) < minLen:
        minLen = len(reducedExample)

##print("==================")
print(minLen)