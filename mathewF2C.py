# File: mathewF2C
# Project: CSIS2101 Assignment 2
# Author: Mathew Doty
# History: Version 1.0 September 4, 2020

# This program converts the given temperature Fahrenheit into Celsius

# greeting
print( "This handy tool will help you convert temperatures!" )

# temperature input
fahrenheit =input( " Please enter temperature in degrees Fahrenheit: ")
mathewFar =float( fahrenheit )

#calculating coversion from Fahrenheit to Celcius
Celsius = (mathewFar - 32) * 5/9

print ( mathewFar, "degrees Fahrenheit equals", Celsius, "Celsius." )
