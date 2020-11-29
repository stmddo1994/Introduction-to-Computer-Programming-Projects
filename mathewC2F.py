# File: mathewC2F
# Project: CSIS2101 Assignment 2
# Author: Mathew Doty
# History: Version 1.0 September 5, 2020

# This program converts the given temperature Celsius to Fahrenheit

# greeting
print( "This handy tool will help you convert temperatures!" )

# temperature input
celsius =input( " Please enter temperature in degrees Celsius: ")
mathewCel =float( celsius )

#calculating coversion from Celsius to Fahrenheit
Fahrenheit = mathewCel * 9/5 + 32

print ( mathewCel, "degrees Celsius equals", Fahrenheit, "Fahrenheit.")
