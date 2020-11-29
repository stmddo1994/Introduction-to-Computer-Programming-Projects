# File: ListFunctionsMathew.py
# Project: CSIS2101 Assignment 8
# Author: Mathew Doty
# History: Version 2.1 October 21, 2020

#This function will provide the range, sum, average, and median
#of a list of inputted numbers along with a list of numbers clipped with
#one more inputted number

def mathewList():
    #start of number list is empty
    number_list = [ ]
    counter = 0
    listlength = 10
    #while loop to input a list of numbers and add them to the list
    while counter < listlength:
        counter += 1
        number = eval(input("Please enter a number to add to the list: "))
        number_list.append(number)

    #number input to clip in a later function
    clipNum = eval(input("Please enter a number to be clipped into the list: "))

    #full starting list
    print("Given List:", number_list)

    #display range
    listrange = rangeList(number_list)
    print("The Range of the List is", listrange)

    #display sum
    listsum = sumList(number_list)
    print("The Sum of the List is", listsum)

    #display average
    listaverage = average(number_list)
    print("The Average of the List is", listaverage)

    #display median
    listmedian = median(number_list)
    print("The Median of the List is", listmedian)

    #display clipped list
    clippedlist = clip(number_list, clipNum)
    print("Clipped List clipped on number", clipNum, "is:\n", clippedlist)

#function for range
def rangeList(number_list):
    #range of a list is the highest number on the list minus the lowest
    fullrange = max(number_list) - min(number_list)
    #return range
    return fullrange

#function for sum
def sumList(number_list):
    fullsum = 0
    #continuously add each item to sum
    for item in number_list:
        fullsum += item
    #verify if created method is the same as the integrated "sum" function
    if fullsum == sum(number_list):
        #return sum if correct
        return fullsum
    #function should never give "Error"
    else:
        return "Error"

#function for average
def average(number_list):
    #average of a list is the sum of all number divided by total numbers given
    #in case of sum function issue
    if sumList(number_list) == "Error":
        fullaverage = "Error in Sum Function"
    #if sum function method is correct
    else:
        #avoid divide by 0 problem
        if len(number_list) == 0:
            fullaverage = 0
        else:
            fullaverage = sumList(number_list) / len(number_list)
    #return average or error message
    return fullaverage

#function for median
def median(number_list):
    #create deep copy of list
    orderedlist = [ ]
    orderedlist += number_list
    #sort list from lowest to heighest value
    orderedlist.sort()

    #find the middle of the total number of items in the list
    middle = (len(orderedlist) - 1) // 2

    #find whether length is odd or even
    if len(orderedlist) % 2 == 0:
        #if the length is even, add the two middle numbers together
        #and find the average between them
        fullmedian = (orderedlist[middle] + orderedlist[middle + 1]) / 2
    else:
        #if the length is odd, the middle found in the above variable
        #will suffice
        fullmedian = orderedlist[middle]
    #return median
    return fullmedian

def clip(number_list, clipNum):
    #make deep copy of list
    haircut = [ ]
    haircut += number_list
    #loop through each item in the list
    for item in haircut:
        #find if item bigger than clipping number
        if item > clipNum:
            #find index number of item to be clipped
            index = haircut.index(item)
            #replace item with clipping number
            haircut[index] = clipNum
    #return new list
    return haircut

#call main function
mathewList()
