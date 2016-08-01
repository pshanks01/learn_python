#!/bin/python

mylist = [1000, 123.456789, 0.00004]
print "A list: %s" % mylist

for item in mylist:
    print "B list: %d" % item

for item in mylist:
    print "C list: %.6f" % item
