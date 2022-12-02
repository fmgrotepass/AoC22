#!/usr/bin/python3 
import re


infile = open("input02", "r")
line = infile.readline()
lookup = dict()
    
lookup["A X\n"]= 4
lookup["A Y\n"]= 8
lookup["A Z\n"]= 3
lookup["B X\n"]= 1
lookup["B Y\n"]= 5
lookup["B Z\n"]= 9
lookup["C X\n"]= 7
lookup["C Y\n"]= 2
lookup["C Z\n"]= 6
gametot = 0
while line:
    gametot = gametot + lookup[line]
    line = infile.readline()
print(gametot)

