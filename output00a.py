#!/usr/bin/python3 
import re

infile = open("input", "r")
line = infile.readline()

gametot = 0
while line:
    gametot = gametot + lookup[inc]
    line = infile.readline()
print(gametot)

