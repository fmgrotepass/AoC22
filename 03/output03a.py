#!/usr/bin/python3 
import re
from collections import Counter

lookup = dict()
lookup['a'] = 1
lookup['b'] = 2
lookup['c'] = 3
lookup['d'] = 4
lookup['e'] = 5
lookup['f'] = 6
lookup['g'] = 7
lookup['h'] = 8
lookup['i'] = 9
lookup['j'] = 10
lookup['k'] = 11
lookup['l'] = 12
lookup['m'] = 13
lookup['n'] = 14
lookup['o'] = 15
lookup['p'] = 16
lookup['q'] = 17
lookup['r'] = 18
lookup['s'] = 19
lookup['t'] = 20
lookup['u'] = 21
lookup['v'] = 22
lookup['w'] = 23
lookup['x'] = 24
lookup['y'] = 25
lookup['z'] = 26
lookup['A'] = 27
lookup['B'] = 28
lookup['C'] = 29
lookup['D'] = 30
lookup['E'] = 31
lookup['F'] = 32
lookup['G'] = 33
lookup['H'] = 34
lookup['I'] = 35
lookup['J'] = 36
lookup['K'] = 37
lookup['L'] = 38
lookup['M'] = 39
lookup['N'] = 40
lookup['O'] = 41
lookup['P'] = 42
lookup['Q'] = 43
lookup['R'] = 44
lookup['S'] = 45
lookup['T'] = 46
lookup['U'] = 47
lookup['V'] = 48
lookup['W'] = 49
lookup['X'] = 50
lookup['Y'] = 51
lookup['Z'] = 52

def dedup(inStr):
    p = ""
    for char in inStr:
        if char not in p:
            p=p+char
    return p

def find_dup_char(input):
 
    # now create dictionary using counter method
    # which will have strings as key and their
    # frequencies as value
    WC = Counter(input)
 
    # Finding no. of  occurrence of a character
    # and get the index of it.
    for letter, count in WC.items():
        if (count > 1):
            return(letter)

            

infile = open("input", "r")
line = infile.readline()

gametot = 0
while line:
    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
    fpd = dedup(firstpart)
    spd = dedup(secondpart)
    inc = find_dup_char(fpd+spd)
    gametot = gametot + lookup[inc]
    line = infile.readline()
print(gametot)

