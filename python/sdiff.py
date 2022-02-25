#!/usr/bin/python3
# Simple script that generates a one-hunk unified diff using simplediff

from simplediff import diff
from sys import argv

if len(argv) < 3:
	print("Pass in two file paths to diff.")
	exit()

file1 = open(argv[1])
file2 = open(argv[2])

print("--- ", argv[1])
print("+++ ", argv[2])

lines1 = file1.readlines()
lines2 = file2.readlines()

print("@@ -1,", len(lines1), " +1,", len(lines2), " @@", sep='')

operators = {
		'=' : '  ',
		'+' : '+ ',
		'-' : '- ',
	}
chunks = diff(lines1, lines2)
for chunk in chunks:
	for line in chunk[1]:
		print(operators[chunk[0]], line, end='')
