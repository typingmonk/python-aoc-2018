railMap = []
carts = []

# > (-,/,\,+) => (>,^,v,?) 
# < (-,/,\,+) => (<,v,^,?)
# ^ (|,/,\,+) => (^,>,<,?)
# v (|,/,\,+) => (V,<,>,?)

NextChar = {
    ">-"   : ">",
    ">/"   : "^",
    ">\\"  : "v",
    
    "<-"   : "<",
    "</"   : "v",
    "<\\"  : "^",
    
    "^|"   : "^",
    "^/"   : ">",
    "^\\"  : "<",
    
    "v|"   : "v",
    "v/"   : "<",
    "v\\"  : ">",
    
    ">+0"  : "^",
    ">+1"  : ">",
    ">+2"  : "v",
    
    "<+0"  : "v",
    "<+1"  : "<",
    "<+2"  : "^",
    
    "^+0"  : "<",
    "^+1"  : "^",
    "^+2"  : ">",
    
    "v+0"  : ">",
    "v+1"  : "v",
    "v+2"  : "<",
}

def getNextXY(x,y,char):
    if(char == ">"):
        return x+1, y
    elif(char == "<"):
        return x-1, y
    elif(char == "^"):
        return x, y-1
    elif(char == "v"):
        return x, y+1
    
def getNextChar(char,rail,turn):
    #print(char,rail,turn)
    if rail == "+":
        code = "".join(char+rail+turn)
    else:
        code = "".join(char+rail)
    return NextChar[code]

def orderSort(carts):
    sortedCart = []
    while len(carts) > 0:
        idx = 0
        if len(carts) > 1:
            for i in range(1,len(carts)):
                if (carts[idx][1] > carts[i][1]) or (carts[idx][1] == carts[i][1] and carts[idx][0] > carts[i][0]):
                    idx = i
        sortedCart.append(carts.pop(idx))
    return sortedCart

#initial
for idx,line in enumerate(open("input.txt")):
    line = line.replace("\t","    ").replace("\n","")
    carts += [(i,idx,char,0) for i, char in enumerate(line) if char in ['>','<','^','v']]
    railMap.append(line.replace(">","-").replace("<","-").replace("^","|").replace("v","|"))

#looping
iterate = 0
crash = []
nCrash = []
while len(crash)==0 and len(nCrash)==0:
    nCarts = []
    iterate += 1
    print(carts)
    for cart in carts:
        nX, nY = getNextXY(cart[0],cart[1],cart[2])
        nChr = getNextChar(cart[2],railMap[nY][nX],str(cart[3]))
        if railMap[nY][nX] == "+":
            nCart = (nX, nY, nChr, (cart[3]+1)%3)
        else:
            nCart = (nX, nY, nChr, cart[3])
        nCrash = [(aCart[0],aCart[1]) for aCart in nCarts if aCart[0] == nCart[0] and aCart[1] == nCart[1]]
        crash = [(aCart[0],aCart[1]) for aCart in  carts if aCart[0] == nCart[0] and aCart[1] == nCart[1]]
        if len(crash)>0 or len(nCrash)>0:
            break
        nCarts.append(nCart)
    #print(nCarts)
    carts = orderSort(nCarts)

print(nCrash)
print(crash)