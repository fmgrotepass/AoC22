#!/usr/bin/python3 
import re

infile = open("input", "r")
line = infile.readline()

gametot = 0
while line:
    line=line.strip(' \n')
    elves=line.split(',')
    elf1range=elves[0].split('-')
    elf2range=elves[1].split('-')
    if(
        (int(elf1range[0]) >= int(elf2range[0]) and  int(elf1range[1]) <= int(elf2range[1]) ) or
        (int(elf1range[0]) <= int(elf2range[0]) and  int(elf1range[1]) >= int(elf2range[1]) )
        ):
        print(line)
        print(elves)
        print(elf1range)
        print(elf2range)
        gametot = gametot + 1   
    line = infile.readline()
print(gametot)

