## 9   players; last marble is worth   25  points: high score is 23
## 10  players; last marble is worth 1618  points: high score is 8317
## 13  players; last marble is worth 7999  points: high score is 146373
## 17  players; last marble is worth 1104  points: high score is 2764
## 21  players; last marble is worth 6111  points: high score is 54718
## 30  players; last marble is worth 5807  points: high score is 37305
## 438 players; last marble is worth 71626 points
##players     = 438
##max_marble  = 71626
players     = 438
max_marble  = 71626

magic_number = 23
score_table = [0 for value in range(players)]
idx_current   = 1
marble_table  = [0,1]
value_current = 1
player_current= 1
last_score = (max_marble // magic_number) * magic_number

while value_current < max_marble:
    if player_current == players:
        player_current  = 1
    else:
        player_current += 1
    value_current += 1
    if value_current % magic_number == 0:
        if idx_current - 7 < 0:
            idx_current = (idx_current - 7) % len(marble_table)
        else:
            idx_current -= 7
        score_table[player_current-1] += marble_table.pop(idx_current) + value_current
    else:
        idx_current   += 2
        if   idx_current == len(marble_table)  :
            marble_table.append(value_current)
            idx_current == len(marble_table) - 1
        elif idx_current == len(marble_table)+1:
            marble_table.insert(1, value_current)
            idx_current = 1
        else:
            marble_table.insert(idx_current, value_current)

print(last_score)
print(score_table)
print(max(score_table))