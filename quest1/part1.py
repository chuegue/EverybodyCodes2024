creatures = open("input1.txt").readlines()[0]


count1 = 0
for c in creatures:
    if c == 'B': count1 += 1
    elif c == 'C': count1 += 3
print(count1)
