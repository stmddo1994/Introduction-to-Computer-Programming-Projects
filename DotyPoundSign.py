# File: DotyPoundSign.py
# Project: CSIS2101 Assignment 5
# Author: Mathew Doty
# History: Version 1.0 September 24, 2020

#This program will display rows of pound signs in from one to the number given
#Each row will add a pound sign
def main():
#input for number of rows
    n = int(input( "Enter number of rows: "))
#validation check
    while n <= 0:
#loop command for when given an invalid number
        n = int(input("Invalid input; Please enter number above 0: "))
#"for" loop on number of rows given
    for y in range (1, n + 1):
#nested "for" loop for number of times to count
        for x in range (1, y + 1):
#print each count as pount sign in single row
            print ("#", end = "")
#ending
        print (" ")
#call function
main()
