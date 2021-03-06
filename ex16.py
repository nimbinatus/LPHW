# import argv
from sys import argv

# set argv
script, filename = argv

# printing
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# asks for input in raw format
raw_input("?")

# prints a line, then opens a file under that filename in write mode (will
# overwrite any file with that filename with this mode).
print "Opening the file..."
target = open(filename, 'w')

# prints a line, then truncates the file at the very beginning. Technically,
# this is not needed due to the 'w' mode, which "truncat[es] the file if it
# already exists" (pydocs).
print "Truncating the file. Goodbye!"
target.truncate()

#prints a line, then asks for three raw inputs
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# prints a line, then inserts the first raw input, then a new line, then the
# second, then a new line, then the third, then a new line all into the target
# file
print "I'm going to write these to the file."

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

# prints a line, then saves and closes the target file
print "And finally, we close it."
target.close()

# new code added from study drill 2
print "Now, though, let's reopen it and then print it out."
target = open(filename)

print "Here is your file."
print target.read()

print "Now we close it again."
target.close()
