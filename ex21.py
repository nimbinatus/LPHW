def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(20, 8)
height = subtract (68, 4)
weight = multiply(60, 2)
iq = divide (240, 2)

print "Age %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
x = (28 + (64 - (120 * (120/2))))
print "By hand, thats (28 + (64 - (120 * (120/2)))) or %d" % x

y = (1 / (2 - (5 * (7 + 3))))
print "If I have the function (1 / (2 - (5 * (7 + 3)))), what is the answer?"
step1 = add (7, 3)
step2 = multiply(5, step1)
step3 = subtract(2, step2)
step4 = divide(1, step3)

print ("So stepwise, that's %d for step 1, %d for step 2, %d for step 3, and "
       "%d for step 4.") % (step1, step2, step3, step4)
print "That equals %d!" % y
