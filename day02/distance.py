def hamming2(s1, s2):
    """Calculate the Hamming distance between two bit strings"""
    assert len(s1) == len(s2)
    if sum(c1 != c2 for c1, c2 in zip(s1, s2)) == 1 :
        print(s1)
        print(s2)
    

with open("input.txt", "r") as ins:
    inputs = []
    for line in ins:
        inputs.append(line.replace("\n",""))

for i in range(len(inputs)):
    for j in range(len(inputs)):
        if i==j :
            continue
        else :
            hamming2(inputs[i], inputs[j])
        




