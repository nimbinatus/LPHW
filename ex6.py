# sets a variable x as a specific string with a decimal variable output
x = "There are %d types of people." % 10
# sets a variable binary with a string value
binary = "binary"
# sets a do_not variable with a string value
do_not = "don't"
# sets a y variable as a specific string with two string variable outputs pulled from the binary and do_not variables
y = "Those who know %s and those who %s." % (binary, do_not)

# prints the value of x
print x
# prints the value of y
print y

# prints a string with a raw data output of x (i.e., the raw string as entered with the output in place)
print "I said: %r." % x
# prints a string with a string data output of y
print "I also said: '%s'." % y

# sets the variable hilarious to False
hilarious = False
# sets the variable joke_evaluation to a string with a raw output
joke_evaluation = "Isn't that joke so funny?! %r"

# prints the variable joke_evaluation with the raw output of hilarious (i.e., False)
print joke_evaluation % hilarious

# sets the variable w to a string
w = "This is the left side of..."
# sets the variable e to a string
e = "a string with a right side."

# prints the value of w and the value of e (concatenates them, in this case)
print w + e
