# import argv function from sys module
from sys import argv

# set up argv
script, input_file = argv

# defines the function print_all, which prints a file passed in the function
# call
def print_all(f):
    print f.read()

# defines a function rewind, which finds the beginning of a file using the
# seek file object and sets the file's current position using absolute file
# positioning
def rewind(f):
    f.seek(0)

# defines a function print_a_line, which prints a value passed in the function
# call and then a line read from the file's current position, keeping the new
# line character intact
def print_a_line(line_count, f):
    print line_count, f.readline()

# opens a file given in the initial argv and sets it to a current_file variable
current_file = open(input_file)

# prints a line
print "First, let's print the whole file:\n"

# calls the print_all function and passes current_file
print_all(current_file)

# prints a line
print "Now, let's rewind, kind of like a tape."

# calls the rewind function and passes current_file
rewind(current_file)

# prints a line
print "Let's print three lines:"

# names and sets the current_line variable
current_line = 1
# calls the print_a_line function and passes current_line and current_file
print_a_line(current_line, current_file)

# resets the current_line variable (iterates)
current_line += 1
# calls the print_a_line function and passes current_line and current_file
print_a_line(current_line, current_file)

# iterates the current_line variable
current_line += 1
# calls the print_a_line function and passes current_line and current_file
print_a_line(current_line, current_file)
