#!/usr/bin/python3.8

import math
import sys 
out = sys.stdout

'''function to calculate the standard error'''
with open("JanOutput.txt", "r") as f:
    jdata = f.readlines()
with open("jSD.txt", "r") as f:
    j_SD = f.readlines()
with open("sSD.txt", "r") as f:
    s_SD = f.readlines()

with open("SeptOutput.txt", "r") as f:
    sdata=f.readlines()

#print(jdata)
lengthj = len(jdata)
lengths=len(sdata)

j_SD = float(j_SD[0].strip())  
s_SD = float(s_SD[0].strip()) 

def SD(SD, length):
    n = math.sqrt(length)
    s_error = SD / n
    return str( s_error)

#to call function for September
sept_s_error = SD(s_SD, lengths)
#print(sept_s_error)

#to call function for Janaury
jan_s_error = SD(j_SD, lengthj)
#print(jan_s_error)

#saving standard error to a file
outj = open('standarderror_jan.txt', 'w')
outs = open('standarderror_sep.txt', 'w')
outj.write(jan_s_error)
outs.write(sept_s_error)
outj.close()
outs.close()

