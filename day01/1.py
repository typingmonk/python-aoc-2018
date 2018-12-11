change_freq = []
for line in open("input.txt"):
    change_freq.append(int(line.strip()))

current = 0
for change in change_freq:
    current += change

print(current)