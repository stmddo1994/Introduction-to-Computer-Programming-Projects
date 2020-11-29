# File: Dotytriangle.py
# Project: CSIS2101 Assignment 6
# Author: Mathew Doty
# History: Version 1.2 October 8, 2020

#import math module
import math

def triangleInput():
    #*could have input using a,b,c = eval(input("Enter 3 sides"))*
    #*saves yourself from calling main function again*
    
    #input side 1 of triangle
    a = int(input("Please enter an integer for the first side of a triangle: "))
    #validate side 1
    while a <= 0:
        a = int(input("Invalid input; Please enter positive integer: "))
    #input side 2    
    b = int(input("Please enter an integer for the second side of a triangle: "))
    #validate side 2
    while b <= 0:
        b = int(input("Invalid input; Please enter positive integer: "))
    #input side 3
    c = int(input("Please enter an integer for the third side of a triangle: "))
    #validate side 3
    while c <= 0:
        c = int(input("Invalid input; Please enter positive integer: "))
    #validation returned false
    if isValid(a, b, c) is False:
        print("Invalid sides; sum of two sides must be greater than remaining side")
        #repeat inputs
        triangleInput()
    #validation returned true
    if isValid(a, b, c) is True:
        #execute area function
        calcArea(a, b, c)
        
#define validation function
def isValid(a, b, c):
#returning boolean conditions
    if a + b <= c or a + c <= b or b + c <= a:
        return False

    else:
        return True
#define area function
def calcArea(a, b, c):
#calculate semiperimeter
    s = (a + b + c)/2
    #calculate area with imported math module with square root
    Area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#display result
    print("The area of the triangle is", Area)
#execute function
triangleInput()
