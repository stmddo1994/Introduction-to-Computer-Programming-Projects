# File: dotyspeedlimit.py
# Project: CSIS2101 Assignment 3
# Author: Mathew Doty
# History: Version 1.3 September 9, 2020

#This program calculates the fines for going over the speed limit

def DotySpeedLimit():
    speedLimitMathew = int ( input ("Speed Limit: "))
    speedMathew = int ( input ("Vehicle Speed: "))
    cOrSZoneMathew = input ("Construction or School Zone (Yes, Y, No, N): ")
# Minimum Fine
    MinFine = 89.00

# Valid Input for Construction/School Zone
    if cOrSZoneMathew != "Yes" and cOrSZoneMathew != "Y" and \
       cOrSZoneMathew != "No" and cOrSZoneMathew != "N":
        print ("Input Invalid!")

# Display Warning for Construction/School Zone
    if cOrSZoneMathew == "Yes" or cOrSZoneMathew == "Y":
       if speedMathew > speedLimitMathew:
           print ("Fine is doubled for speeding in a school zone!")

# Calculating Fine and Display for Speed and Speed Limit
    if speedMathew <= speedLimitMathew:
        print ("You are driving within the speed limit. Good job!")

# Less than 5 MPH Over Speed Limit
    elif speedMathew < speedLimitMathew + 5:
        if cOrSZoneMathew != "Yes" and cOrSZoneMathew != "Y":
            TotalFine = MinFine
        else:
            TotalFine = MinFine * 2
        print ("Total Fine Calculated = $",f"{TotalFine: 0.2f}")
        print ("Slow down. !")

# Less than 15 MPH
    elif speedMathew < speedLimitMathew + 15:
        if cOrSZoneMathew != "Yes" and cOrSZoneMathew != "Y":
            TotalFine = MinFine + 40
        else:
            TotalFine = (MinFine + 40) * 2
        print ("Total Fine Calculated = $",f"{TotalFine: 0.2f}")
        print ("Drive with Caution. !")

# Less than 25 MPH
    elif speedMathew < speedLimitMathew + 25:
        if cOrSZoneMathew != "Yes" and cOrSZoneMathew != "Y":
            TotalFine = MinFine + 100
        else:
            TotalFine = (MinFine + 100) * 2
        print ("Total Fine Calculated = $",f"{TotalFine: 0.2f}")
        print ("You are over speeding. !")

# Less than 30 MPH
    elif speedMathew < speedLimitMathew + 30:
        if cOrSZoneMathew != "Yes" and cOrSZoneMathew != "Y":
            TotalFine = MinFine + 190
        else:
            TotalFine = (MinFine + 190) * 2
        print ("Total Fine Calculated = $",f"{TotalFine: 0.2f}")
        print ("You are in Danger zone. !")

# Maximum Fine/30 MPH or more
    elif speedMathew >= speedLimitMathew + 30:
        print ("Court Mandatory - Fine decided in court")
        print ("See ya in court. !!")

    

DotySpeedLimit()
