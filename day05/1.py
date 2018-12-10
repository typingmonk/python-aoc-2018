with open("input.txt") as exampleFile:
    example = exampleFile.readline()
##print(example)

example = list(example)
index = 0
while index < len(example)-1:
    ##print("=====================")
    ##print("index        : ",index)
    ##print("len(example) : ",len(example))
    poly1 = example[index]
    poly2 = example[index+1]
    ##print("poly1        : ",poly1)
    ##print("poly2        : ",poly2)
    if (poly1.upper() == poly2 and poly1 == poly2.lower()) or (poly1.lower() == poly2 and poly1 == poly2.upper()):
        del example[index:index+2]
        if index > 0:
            index -= 1
    else:
        index += 1

print("left len : ",len(example))