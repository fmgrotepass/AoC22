#!/usr/bin/python3 
import re


infile = open("input01", "r")
line = infile.readline()
elf = 0
cals = 0
elfcal = []
maxcals = 0
maxelf = 0
while line:
    linecal = line
    if(linecal == "\n"):
        elfcal.append(cals)
        print(f"at run {elf} we are  with {cals} and current max {maxelf} had {maxcals}" )
        if (cals > maxcals):
            maxcals = cals
            maxelf = elf
        cals = 0
        elf = elf + 1
    else:
        cals = cals+int(linecal)
        print(f"at run {elf} we are  with {cals}" )
        
    line = infile.readline()
elfcal.sort(reverse=True)
etot = elfcal[0] +elfcal[1] +elfcal[2] 
print(elfcal[0])
print(etot)

