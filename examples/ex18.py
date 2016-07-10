#!/bin/python

def foo(*args):
    arg1,arg2 = args
    print "foo() arg1: %s \nfoo() arg2: %s" % (arg1,arg2)

def bar(arg1,arg2):
    print "bar() arg1: %s \nbar() arg2: %s" % (arg1,arg2)

def baz():
    print "baz() no args"

foo("eeny","meeny")
bar("miney","moe")
baz()
