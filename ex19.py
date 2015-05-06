# defines a function cheese_and_crackers with two inputs
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# prints a line with one input (called) as a signed integer decimal number
    print "You have %d cheeses!" % cheese_count
# prints a line with one input (called) as a signed integer decimal number
    print "You have %d boxes of crackers!" % boxes_of_crackers
# prints a line
    print "Man, that's enough for a party!"
# prints a line
    print "Get a blanket.\n"

# prints a line
print "We can just give the function numbers directly:"
# calls the function cheese_and_crackers and passes 20 and 30 to it
cheese_and_crackers(20, 30)

# prints a line
print "OR, we can use variables from our script:"
# names and sets a variable
amount_of_cheese = 10
# names and sets a variable
amount_of_crackers = 50

# calls the function cheese_and_crackers and passes previously named variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# prints a line
print "We can even do math inside, too:"
# calls the function cheese_and_crackers and passes two expressions
cheese_and_crackers(10 + 20, 5 + 6)

# prints a line
print "And we can combine the two, variables and math:"
# calls the function and passes two expressions, each with previous vars
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
