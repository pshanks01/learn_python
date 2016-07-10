#!/bin/python

from sys import argv
from os.path import exists

script, source, dest = argv

print "Copying from %s to %s" % (source,dest)

infile = open(source)
indata = infile.read()

print "source file is %d bytes long" % len(indata)

print "Does destination file exist? %r" % exists(dest)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input(">")

outfile = open(dest, 'w')
outfile.write(indata)

print "Finished"

infile.close()
outfile.close()
