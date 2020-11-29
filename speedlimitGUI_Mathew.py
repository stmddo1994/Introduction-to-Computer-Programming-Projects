# File: speedlimitGUI_Mathew.py
# Project: CSIS2101 Assignment 12
# Author: Mathew Doty
# History: Version 2.0 November 7, 2020

#This program will create a GUI to calculate the fine recieved for speeding

#Import tkinter function for creating a GUI
import tkinter

#Create a class that will make a GUI
class SpeedingFines:
    #Create the init function for the boxes and text
    def __init__(self):
        #Create main GUI window
        self.main_window = tkinter.Tk()

        #Create frames for each line of labels and entries, answers, or buttons
        self.top_frame = tkinter.Frame(self.main_window)
        self.frame_2 = tkinter.Frame(self.main_window)
        self.frame_3 = tkinter.Frame(self.main_window)
        self.frame_4 = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #Top Label for Speed Limit
        self.spdlmt_label = tkinter.Label(self.top_frame,
                                          text = "Enter Speed Limit: ")

        #Entry for Speed Limit
        self.spdlmt_entry = tkinter.Entry(self.top_frame,
                                          width = 10)

        #Pack Top Label and Entry
        self.spdlmt_label.pack(side = "left")
        self.spdlmt_entry.pack(side = "left")

        #Second Label and Entry for Speed of Vehicle
        self.speed_label = tkinter.Label(self.frame_2,
                                         text = "Enter Vehicle Speed: ")

        self.speed_entry = tkinter.Entry(self.frame_2,
                                         width = 10)

        #Pack Label and Entry
        self.speed_label.pack(side = "left")
        self.speed_entry.pack(side = "left")

        #Third Label and Entry for Construction or School Verification
        self.csz_label = tkinter.Label(self.frame_3,
                                       text = "Construction or School Zone? (Yes, Y, No, N): ")

        self.csz_entry = tkinter.Entry(self.frame_3,
                                       width = 10)

        #Pack Label and Entry
        self.csz_label.pack(side = "left")
        self.csz_entry.pack(side = "left")

        #Fourth frame for Display of Results
        #Create Blank Variable String
        self.display = tkinter.StringVar()

        #Label for Displaying Results
        self.display_label = tkinter.Label(self.frame_4,
                                           textvariable = self.display)

        #Pack Label with Padding Sizes for X and Y Axis
        self.display_label.pack(padx = 20, pady = 20)

        #Bottom Frame for Buttons
        #Enter Button to call SpeedLimit function
        self.enter_button = tkinter.Button(self.bottom_frame,
                                           text = "Enter",
                                           command = self.SpeedLimit)
        #Quit Button to destroy main window
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text = "Quit",
                                          command = self.main_window.destroy)

        #Pack Buttons
        self.enter_button.pack(side = "top")
        self.quit_button.pack(side = "top")

        #Pack all frames to form GUI
        self.top_frame.pack()
        self.frame_2.pack()
        self.frame_3.pack()
        self.frame_4.pack()
        self.bottom_frame.pack()

        #Enter the Main Loop
        tkinter.mainloop()

    #Creates function that calculates speed limit fines when "Enter" Button is clicked
    def SpeedLimit(self):
        #Variables created by recieving Entries
        speedlimit = int(self.spdlmt_entry.get())
        speed = int(self.speed_entry.get())
        cOrSZone = self.csz_entry.get()

        #Calculate difference
        diff = speed - speedlimit
        #Empty variables
        fine = 0
        display = ""
        csz_display = ""

        #Decide what fines depending on the calculated difference
        #Create display along with fine
        if diff > 0 and diff < 5:
            fine = 89.00
            display += "Slow down!"
        elif diff >= 5 and diff < 15:
            fine = 129.00
            display += "Drive with Caution!"
        elif diff >= 15 and diff < 25:
            fine = 189.00
            display += "You are overspeeding!"
        elif diff >= 25 and diff < 30:
            fine = 279.00
            display += "Call Kenny Loggins, because you're in the Danger Zone!"
        elif diff >= 30:
            display += "You must go to Court to recieve your fine."
        else:
            display += "Good Job! You're within the Speed Limit!"

        #Double fine if in Construction or School Zone
        if cOrSZone == "Yes" or cOrSZone == "Y":
            fine *= 2
            if diff > 0 and diff < 30:
                csz_display += "Fine is doubled for speeding in a Construction or School Zone"
        elif cOrSZone == "No" or cOrSZone == "N":
            fine = fine
        #Display Error Message if Input invalid
        else:
            csz_display += "Invalid Input; Please enter Yes, Y, No, or N."

        #Empty variable for full diplay
        full_display = ""

        #Display only error message if C or S Zone has incorrect input
        if cOrSZone != "Yes" and cOrSZone != "Y" and cOrSZone != "No" and cOrSZone != "N":
            full_display += csz_display
        #Create string to make a full display
        else:
            full_display += "Speed Limit: " + str(speedlimit) + "\n \n"
            full_display += "Vehicle Speed: " + str(speed) + "\n \n"
            full_display += "Construction or School Zone: " + cOrSZone + "\n" + csz_display + "\n \n"
            full_display += "Total Fine Calculated = $" + str(f"{fine:0.2f}") + "\n" + display

        #Set string into Display frame
        self.display.set(full_display)

#Call function
if __name__ == "__main__":
    speedfines = SpeedingFines()
    
