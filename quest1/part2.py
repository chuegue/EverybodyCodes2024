creatures = open("input2.txt").readlines()[0]

count2 = 0
potions = {'x' : 0, 'A' : 0, 'B' : 1, 'C' : 3, 'D' : 5}
for i in range(0, len(creatures)-1, 2):
    c1 = creatures[i]
    c2 = creatures[i+1]
    if c1 == 'x' or c2 == 'x':
        count2 += potions[c1] + potions[c2]
    else:
        count2 += potions[c1] + 1 if c2 != 'x' else potions[c1]
        count2 += potions[c2] + 1 if c1 != 'x' else potions[c2]
print(count2)




