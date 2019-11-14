#!/bin/python3
import os
import sys
filename = 'test.txt'

# If no File is given, use STDIN instead!
if os.path.isfile(filename):
  handle = open(filename, 'r')
else:
  print(f'File {filename} does not exist! Reading from STDIN')
  handle = sys.stdin


# the with-statement automatically closes the file after execution
# https://effbot.org/zone/python-with-statement.htm
with handle as h:
  lines = h.readlines()  # Read the whole file into memory

num = 0
width = len(str(len(lines))) # get the number of decimal places
for line in lines:
  print(f'{num:{width}}: {line.rstrip()}') # https://www.python.org/dev/peps/pep-0498/#format-specifiers
  num += 1
