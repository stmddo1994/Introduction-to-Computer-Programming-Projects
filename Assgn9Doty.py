# File: Assgn9Doty.py
# Project: CSIS2101 Assignment 9
# Author: Mathew Doty
# History: Version 1.4 October 27, 2020

#This program will give three seperate functions to edit inputted strings
#The first will replace the last of the inputted substring with an inputted new one
#The second will convert an inputted phone number with letters into its numbered counterpart
#The third will convert an inputted phrase into a version of pig latin

def main():
    #Call all functions to main
    mDReplace()
    mDNumberConverter()
    mDPigLatin()

#First function
def mDReplace():
    #Give the inputs
    string = input("Please enter a string: ")
    oldsub = input("Please enter a substring within the string you entered: ")
    newsub = input("Please enter a substring to replace the old one: ")

    #Find the areas where the old substrings appear
    #Give them a character that will split them up
    splitter = string.replace(oldsub, "/" + oldsub)

    #Split them into a list
    splitstring = splitter.split("/")

    #Find the item on the list that is last
    lastsub = splitstring[len(splitstring) - 1]

    #Replace old substring with new substring
    replacement = lastsub.replace(oldsub, newsub)

    #Delete old substring
    del(splitstring[len(splitstring)-1])

    #While loop to turn list into new string
    n = 0
    newstring = ""
    while n < len(splitstring):
        newstring += splitstring[n]
        n += 1

    #Add string with replaced substring
    newstring += replacement

    #Display new string
    print(newstring)

#Second function
def mDNumberConverter():
    #Give phone number input
    phone_number = input("Please enter a 7 or 10 digit telephone number: ")

    #Convert any lower case letters into uppercase
    phone_upper = phone_number.upper()

    #Create new string
    phone_replace = ""

    #Use for loop to replace each letter with correct number if needed
    for item in phone_upper:
        if item == "A" or item == "B" or item == "C":
            item = "9"
        elif item == "D" or item == "E" or item == "F":
            item = "8"
        elif item == "G" or item == "H" or item == "I":
            item = "7"
        elif item == "J" or item == "K" or item == "L":
            item = "6"
        elif item == "M" or item == "N" or item == "O":
            item = "5"
        elif item == "P" or item == "Q" or item == "R" or item == "S":
            item = "4"
        elif item == "T" or item == "U" or item == "V":
            item = "3"
        elif item == "W" or item == "X" or item == "Y" or item == "Z":
            item = "2"
        #Add character to new string
        phone_replace += item

    #Display translated phone number
    print(phone_replace)

#Third Function
def mDPigLatin():
    #Give phrase input
    english = input("Please enter the phrase you wish to translate: ")

    #Split words into list
    splitup = english.split(" ")

    #Create new list
    newlist = [ ]

    #Use For loop to convert words
    for item in splitup:
        #Keep untranslated item
        olditem = item
        #Find last letter
        lastletter = item[len(item) - 1]
        #Ensure character is in alphabet and loop until found
        while lastletter.isalpha() == False and lastletter.isdigit() == False:
            item = item.rstrip(lastletter)
            lastletter = item[len(item) - 1]
        #Create place to put new word
        newitem = ""
        #Place last letter in front and add word with last letter removed
        newitem = lastletter + item.rstrip(lastletter)
        #Put each word in list
        newlist.append(newitem)
        #Add XX to list next to translated word
        newlist.append("XX")
        #Add space if word is before the end
        if splitup.index(olditem) < len(splitup) - 1:
            newlist.append(" ")

    #Use for loop to combine parts of list together in new string
    p = 0
    piglatin = ""
    while p < len(newlist):
        piglatin += newlist[p]
        p += 1

    #Display translated phrase
    print(piglatin)

main()
