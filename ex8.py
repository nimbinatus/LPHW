# sets a variable formatter with four raw data inputs
formatter = "%r %r %r %r"

# passes formatter four numerals and prints it
print formatter % (1, 2, 3, 4)
# passes formatter four strings and prints it (formatter will print the raw strings)
print formatter % ("one", "two", "three", "four")
# passes formatter four Booleans and prints it
print formatter % (True, False, False, True)
# passes formatter four variables and prints it (formatter will print the raw string with the %rs intact)
print formatter % (formatter, formatter, formatter, formatter)
# passes formatter four strings and prints it (formatter will print the raw strings; it uses single quotes unless forced by apostrophes or other quote marks for efficiency reasons)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.", # TypeError here on first run due to comma forgotten
    "So I said goodnight."
)
