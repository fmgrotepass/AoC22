#!/usr/bin/python3 
import re
from collections import Counter

infile = open("input", "r")
line = infile.readline()

def find_dup_char(input):
 
    # now create dictionary using counter method
    # which will have strings as key and their
    # frequencies as value
    WC = Counter(input)
 
    # Finding no. of  occurrence of a character
    # and get the index of it.
    for letter, count in WC.items():
        if (count > 1):
            return(True)
    return(False)

gametot = 0
missing = True
while missing:
    substr = line[gametot:gametot+14]
    missing = find_dup_char(substr)
    gametot = gametot + 1
print(gametot)

