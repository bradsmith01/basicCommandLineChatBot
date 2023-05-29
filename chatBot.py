#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 19:06:54 2023

@author: bradleysmith
===================================
A chat bot to open folders check 
percent difference and also 
calculate the days differnce 
between two dates 
"""

#Import Module 
import MyChatBotFuncs

while True:
    # User Input to repeat
    userInput = input("\nHow can I help?...\n").lower()
    
    #This is the only Quit that will end the loop. 
    #The Other quit statements will just exit the function it is running.
    if "q" in userInput or "quit" in userInput:
        break

    # If the word "create" is in the User Input, it will search for other words
    elif "create" in userInput:
        
        # If the word "folder" is in the input, it will 'CREATE' -> 'Folder'.
        if "folder" in userInput:
            
            # Ask User for name of Folder and Location
            folderName = str(input("Name of the Folder?...\n"))
            folderLocation = str(input("""Where would you like the folder to be created:
1) Desktop,
2) Downloads,
3) Documents,
Press q to quit\n""")).lower()

            #Run the createFolder function from the Module
            MyChatBotFuncs.createFolder(folderLocation, folderName)
            continue
        
    #If there is the word calculate in the users Input
    elif "calc" in userInput or "calculate" in userInput:
        
        #Then if the word date is in the user input along with calc will calculate date
        if "date" in userInput or "dates" in userInput:
            print("To calculate the date difference, enter the dates as follows:\nFirst Date:\n1) Day,\n2) Month,\n3) Year.\nAnd the same for the second Date.")
            fDateDay = str(input("First Date - Day: "))
            fDateMonth = str(input("First Date - Month: "))
            fDateYear = str(input("First Date - Year: "))
            sDateDay = str(input("Second Date - Day: "))
            sDateMonth = str(input("Second Date - Month: "))
            sDateYear = str(input("Second Date - Year: "))
            MyChatBotFuncs.calcDateFromCurrent(fDateDay, fDateMonth, fDateYear, sDateDay, sDateMonth, sDateYear)
            continue
        
        #or if the word percent is in the user input along with calc the percent difference between 2 numbers
        elif "percent" in userInput or "%" in userInput:
            firstNumber = str(input("What is the first number to compare?\n"))
            if firstNumber == "q" or firstNumber == "quit":
                continue
            secondNumber = str(input("What is the second number to compare?\n"))
            if secondNumber == "q" or secondNumber == "quit":
                continue
            MyChatBotFuncs.percentChange(firstNumber, secondNumber)
            continue
        
