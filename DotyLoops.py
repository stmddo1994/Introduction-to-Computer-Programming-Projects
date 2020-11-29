# File: DotyLoops.py
# Project: CSIS2101 Assignment 4
# Author: Mathew Doty
# History: Version 1.3 September 14, 2020

# This function will demonstrate different loops

def loops():
#Loop counting down from 10
    for num in range (10, 0, -1):
        print (num, end = " ")

    print(" ")
#Loop counting up to 30 by 3s
    for num in range (3, 30, 3):
        print (num, end = ",")
#Keeping commas up until the end
    print("30")
#Integer "while" loop
    n = int(input("Please enter integer perimeter: "))
#Keep integer even
    evenn = n // 2 * 2
#Validation check
    while n < 0 or n > 10000:
        n = int(input("Invalid input, Please enter integer again: "))

    counter = 2
#"While" loop
    while evenn >= 0:
        print(evenn, end = " ")
        evenn -= counter

    print (" ")
#Integer "for" loop
    x = int(input("Please enter new integer perimeter: "))
#Validation check
    while x < 0 or x > 10000:
        x = int(input("Invalid input, Please enter integer again: "))

    for num in range (1, x+1, 2):
        print (num, end = " ")

    print (" ")
        
    
loops()
