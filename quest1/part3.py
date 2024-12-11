creatures = open("input3.txt").readlines()[0]

potions = {'x': 0, 'A': 0, 'B': 1, 'C': 3, 'D': 5}
count = 0
for i in range(0, len(creatures) - 2, 3):
    squad = creatures[i:i+3]
    xcount = squad.count('x')
    if xcount >= 2:
        count += sum([potions[c] for c in squad])
    elif xcount == 1:
        count += sum([potions[c] for c in squad]) + 1 * (3 - xcount)
    elif xcount == 0:
        count += sum([potions[c] for c in squad]) + 2 * (3 - xcount)
    
print(count)
