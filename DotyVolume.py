# File: DotyVolume.py
# Project: CSIS2101 Assignment 7
# Author: Mathew Doty
# History: Version 1.4 October 15, 2020

#Import math module
import math
    
#function to solve volume of cube
def cubeVolMathew(s):
    volume = s ** 3
    return volume

#function for volume of sphere
def sphereVolMathew(r):
    volume = (4 / 3) * math.pi * (r ** 3)
    return volume

#function for volume of cylinder
def cylVolMathew(r,h):
    volume = math.pi * (r ** 2) * h
    return volume

#function for volume of cone
def coneVolMathew(r,h):
    volume = (1 / 3) * math.pi * (r ** 2) * h
    return volume
