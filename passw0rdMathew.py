# File: passw0rdMathew.py
# Project: CSIS2101 Assignment 10
# Author: Mathew Doty
# History: Version 1.0 November 3, 2020

#This program should take the passwords found in one file and write down in another
#if a password is accepted or, if not, why it is not accepted

def main():
    #try and accept in case the file is not found
    try:
        #open the input file containing passwords to be read
        iFile = open("input_file_passwdin.txt", "r")
        #create a new output file to write
        oFile = open("mathewpasswdout.txt", "w")
    #Gives message in case of this error
    except IOError:
        print("File does not exist")

        #read line from input
    line = iFile.readline()

    #loop for each line in file
    while line != "":
        #seperate by enter
        line = line.rstrip("\n")
        
        #change line to called validation function
        line = checkPassw0rdMathew(line)

        #Write line into output file
        oFile.write(line + "\n")

        #Read line to stop loop
        line = iFile.readline()

    #Indicate output is finished
    print("File output Done!")


    #close input and output files
    iFile.close()
    oFile.close()

#function to validate and add to password
def checkPassw0rdMathew(psswd):
    #variables to validate password lines
    lPass = len(psswd)
    uCasecount = 0
    lCasecount = 0
    dCount = 0
    isSymbol = False

    #read each character in each line
    for ch in psswd:
        #check if character is a letter
        if ch.isalpha():
            #check if letter is uppercase or lowercase
            if ch.isupper():
                uCasecount += 1      
            else:
                lCasecount += 1
        #check if character is a digit      
        elif ch.isdigit():
            dCount += 1
        #if character is none of these, it's a symbol
        else:
            isSymbol = True
                
    #If password is at least 8 characters long
    #Has 2 uppercase and lowercase letters
    #Has at least one digit and DOES NOT have a symbol...
    if lPass >= 8 and uCasecount >= 2 and lCasecount >= 2 \
       and dCount > 0 and isSymbol == False:
        #Add acceptance to the line
        psswd += " - Password Accepted"
            
    #If any conditions were not met...
    else:
        #Add decline to the line and any reasons why
        psswd += " - Password is not accepted."
        if lPass < 8:
            psswd += "\n Password is not 8 characters long."
        if uCasecount < 2:
            psswd += "\n Password does not have 2 uppercase characters."
        if lCasecount < 2:
            psswd += "\n Password does not have 2 lowercase characters."
        if dCount == 0:
            psswd += "\n Password should have at least one digit."
        if isSymbol == True:
            psswd += "\n Password should not contain any special characters."

    #return new password line
    return psswd

#Call main function
if __name__ == "__main__":
    main()
