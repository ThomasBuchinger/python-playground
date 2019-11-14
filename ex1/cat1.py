#!/bin/python3
filename = 'test.txt'

# the with-statement automatically closes the file after execution
# https://effbot.org/zone/python-with-statement.htm
with open(filename, 'r') as f:
  num = 0
  for line in f:
    print('%3d: %s' % (num, line.rstrip()))
    num += 1
