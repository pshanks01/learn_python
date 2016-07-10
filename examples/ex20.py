#!/bin/python

from sys import  argv

script, infile = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print1(count,f):
    print count, f.readline()

curr_file = open(infile)

print "First print whole file:\n"
print_all(curr_file)

print "Now rewind"
rewind(curr_file)

print "Print 3 lines"
curr_line = 1
print1(curr_line,curr_file)

curr_line += 1
print1(curr_line,curr_file)

curr_line += 1
print1(curr_line,curr_file)

curr_file.close()
