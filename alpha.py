#!/usr/bin/python3.8

import sys 
out = sys.stdout

USER_PROMPT = "Please enter your desired confidence level\n"
OUTPUT_FILE = "alpha.txt"

#getting confidence level 
cl = float(input(USER_PROMPT))

#calculating alpha
alpha = (1-cl)/2

#saving alpha value to a file
out = open(OUTPUT_FILE, 'w')
out.write(str(alpha) + "\n")
out.close()
