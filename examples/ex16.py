from sys import argv

script,filename = argv

print "Going to erase %r." % filename
print "if you don't want that, hit CTRL-C now."
print "if this is acceptable, hit RETURN"

raw_input("?")

print "Opening the file..."
target = open(filename,'w')

print "Truncating the file."

target.truncate()

print "Now provide three lines of input"
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "Writing these to the file %s" % filename

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "Closing the file"
target.close()
