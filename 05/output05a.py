#!/usr/bin/python3 
import re
infile = open("input", "r")
line = infile.readline()
part1 = True
gametot = 0
stacks = []
for i in range(9):
    stacks.append([])

while line:
    print(line)
    if part1 == True:
        if line == "\n":
            part1 = False
            line = infile.readline()
            continue
        if line.__contains__("1   2   3   4   5   6   7   8"):
            line = infile.readline()
            continue
        for i in range(9):
            lineC = list(line)

            crate = lineC[1+4*i]

            if crate !=' ':
                stacks[i].insert(0,crate)
    else:

        step = line.split(' ')
        print(step)
        count = int(step[1])
        src = int(step[3])-1    
        dest = int(step[5]) -1
        print(f"{count} {src} {dest} {stacks[src]} {stacks[dest]}")
        for i in range(count):
            crate = stacks[src].pop()
            stacks[dest].append(crate)

    gametot = gametot 
    line = infile.readline()
out = "" 
for i in range(9):

    out = out + stacks[i].pop()
print(out)
print(gametot)

