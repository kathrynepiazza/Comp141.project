#!/usr/bin/python3.8

import numpy as np
import sys
out = sys.stdout

with open("JanOutput.txt", "r") as f:
    jdata = f.readlines()
with open("SeptOutput.txt", "r") as f:
    sdata = f.readlines()

i = 0
while i < len(jdata):
    jdata[i].strip()
    jdata[i] = int(jdata[i])
    sdata[i].strip()
    sdata[i] = int(sdata[i])
    i+=1
def find_sd(arr):
    SD = np.std(arr)
    return SD
j_SD = find_sd(jdata)
s_SD = find_sd(sdata)

out = open('jSD.txt', 'w')
out.write(str(j_SD))
out.close()
out = open('sSD.txt', 'w')
out.write(str(s_SD))
out.close()
