# name and set some variables
# this variable assignment names the variable "cars" and sets it equal to a value of 100 
cars = 100
# names the variable "space_in_a_car" and sets it equal to a value of 4.0
space_in_a_car = 4.0
# names the variable "drivers" and sets it equal to a value of 30
drivers = 30
# names the variable "passengers" and sets it equal to a value of 90
passengers = 90
# names the variable "cars_not_driven" and sets it equal to the result of 100 minus 30
cars_not_driven = cars - drivers
# names the variable "cars_driven" and sets it equal to "drivers", which is currently 30
cars_driven = drivers
# names the variable "carpool_capacity" and sets it equal to 30 * 4.0
carpool_capacity = cars_driven * space_in_a_car
# names the variable "average_passengers_per_car" and sets it equal to 90 divided by 30
average_passengers_per_car = passengers / cars_driven


# printing a series of statements with the values of the variables embedded within them
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
