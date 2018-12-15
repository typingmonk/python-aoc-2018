rules   = list()
results = list()
for i, line in enumerate(open("input.txt")):
    if i >  1:
        pairs   = line.strip().replace(" ","").split("=>")
        rules.append(pairs[0])
        results.append(pairs[1])
    if i == 0:
        state = line.strip().split(" ")[2]
state = [i for i, chr in enumerate(state) if chr == "#"]

iterate = 0
while iterate<50000000000:
    iterate += 1
    start = state[0] - 2
    end = state[-1] + 2
    state_set = set(state)
    state = list()
    rules_set = set(rules)
    for i in range(start, end + 1):
        snippet = list()
        for idx in range(i-2,i+3):
            if idx in state_set:
                snippet.append("#")
            else:
                snippet.append(".")
        snippet = "".join(snippet)
        if snippet in rules_set and "#" == results[rules.index(snippet)]:
            state.append(i)
    if iterate == 50 or iterate == 500 or iterate == 5000 or iterate == 50000:
        print("iterate : ",iterate)
        print("sum : ",sum(state))
print(sum(state))

"""iterate :  5000
sum :  325956
iterate :  5000 0
sum :  3250956
iterate :  5000 0000000
sum :  3250000000956"""