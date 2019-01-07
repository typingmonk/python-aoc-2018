input  = 598701
target = "598701"
idx_elf0 = 0
idx_elf1 = 1
recipes = [3,7]

while True:
    addUp = recipes[idx_elf0] + recipes[idx_elf1]
    # append new recipes
    if addUp > 9 :
        recipes.append(1)
        recipes.append(addUp%10)
    else:
        recipes.append(addUp)
    # renew the current recipes
    idx_elf0 = (idx_elf0 + recipes[idx_elf0] + 1) % len(recipes)
    idx_elf1 = (idx_elf1 + recipes[idx_elf1] + 1) % len(recipes)
    #print(recipes)
    #print(''.join(map(str,recipes[-6:])))
    if len(recipes) >= 7:
        if ''.join(map(str,recipes[-6:])) == target:
            print(len(recipes) - 6)
            break
        if ''.join(map(str,recipes[-7:-1])) == target:
            print(len(recipes) - 7)
            break
