# File: DotyVolumes.py
# Project: CSIS2101 Assignment 7
# Author: Mathew Doty
# History: Version 1.3 October 15, 2020

#This program will make a menu for finding the volumes of 3D objects

#Import file
import DotyVolume

#menu function
def DotyMenu():
    choice = 0
    #while function for exit
    while choice != 5:
        #call display function
        menuMathew()
        #input for menu number
        choice = int(input("Please enter 1 2 3 4 or 5: "))
        
        #1 is entered as input, finding volume of cube
        if choice == 1:
            print("We will now calulate the volume of a cube.")
            #input for side size
            side = eval(input("Please enter the length of a side of the cube in inches: "))
            #calling validation function to make sure input is above 0
            while validInput(side) is False:
                #repeat input if function returns false
                side = eval(input("Invalid input; please enter a positive number: "))
            #display volume and call function while keeping rounded to 2 decimals
            volume = DotyVolume.cubeVolMathew(side)
            print("The volume of a cube with side", side, "inches is:", \
                  f"{volume:0.2f}", "cubic inches.")
            
        #2 input, finding volume of sphere    
        elif choice == 2:
            print("We will now calculate the volume of a sphere.")
            #input for radius size
            radius = eval(input("Please enter the radius of the sphere in inches: "))
            #calling validation function
            while validInput(radius) is False:
                radius = eval(input("Invalid input; please enter a positive number: "))
            #display volume and call function
            volume = DotyVolume.sphereVolMathew(radius)
            print("The volume of a sphere with radius", radius, "inches is:", \
                  f"{volume:0.2f}", "cubic inches.")
            
        #3 input, finding volume of cylinder    
        elif choice == 3:
            print("We will now calculate the volume of a cylinder.")
            #input for radius size
            radius = eval(input("Please enter the radius of the cylinder in inches: "))
            #calling validation function
            while validInput(radius) is False:
                radius = eval(input("Invalid input; please enter a positive number: "))
            #input for height
            height = eval(input("Please enter the height of the cylinder in inches: "))
            #calling validation function
            while validInput(height) is False:
                height = eval(input("Invalid input; please enter a positive number: "))
            #display volume and call function
            volume = DotyVolume.cylVolMathew(radius,height)
            print("The volume of a cylinder with radius", radius, "inches and a height of", \
                  height, "inches \n is:", f"{volume:0.2f}", "cubic inches.")
            
        #4 input, finding volume of cone    
        elif choice == 4:
            print("We will now calculate the volume of a cone.")
            #input for radius size
            radius = eval(input("Please enter the radius of the cone in inches: "))
            #calling validation function
            while validInput(radius) is False:
                radius = eval(input("Invalid input; please enter a positive number: "))
            #input for height
            height = eval(input("Please enter the height of the cone in inches: "))
            #calling validation function
            while validInput(height) is False:
                height = eval(input("Invalid input; please enter a positive number: "))
            #display volume and call function
            volume = DotyVolume.coneVolMathew(radius,height)
            print("The volume of a cone with radius", radius, "inches and a height of", \
                  height, "inches \n is:", f"{volume:0.2f}", "cubic inches.")
            
        #5 input, exit    
        elif choice == 5:
            print("Bye!")
            
        #invalid input varification for menu    
        else:
            choice = print("Invalid input")
            
#menu display function to give user instructions for what to type
def menuMathew():
    print("1. Volume of a cube in cubic inches.")
    print("2. Volume of a sphere in cubic inches.")
    print("3. Volume of a cylinder in cubic inches.")
    print("4. Volume of a cone in cubic inches.")
    print("5. Exit the program")

#validation function
def validInput(i):
    if i > 0:
        return True
    else:
        return False
    
#call main/menu function
DotyMenu()
