dictionary = []
text = []

input_lines1 = open("input1.txt").readlines()

dictionary = input_lines1[0].split(':')[1].strip().split(',')

text = input_lines1[2].strip().split()

count1 = 0
for word in text:
    for rune in dictionary:
        if rune in word:
            count1 += 1

print(count1)

input_lines2 = open("input2.txt").readlines()
runic_words = input_lines2[0].split(':')[1].strip().split(',')
shield_words = []
for i in range(2, len(input_lines2)):
    shield_words += input_lines2[i].strip().split()

import re

count2 = 0
for word in shield_words:
    seen = set()
    for rune in runic_words:
        sub = f"(?=({rune}))"
        for i in re.finditer(sub, word):
            for j in range(i.start(), i.start() + len(rune)):
                seen.add(j)
        sub = f"(?=({rune[::-1]}))"
        for i in re.finditer(sub, word):
            for j in range(i.start(), i.start() + len(rune)):
                seen.add(j)
    count2 += len(seen)
    #if len(seen) > 0: print(f"{word}:{len(seen)}")

print(count2)

input_lines3 = open("input3.txt").readlines()
runic_words = input_lines3[0].split(':')[1].strip().split(',')
matrix = []
for i in range(2, len(input_lines3)):
    matrix.append(list(input_lines3[i].strip()))
matrix_t = list(zip(*matrix))
print(matrix)
print(matrix_t)
