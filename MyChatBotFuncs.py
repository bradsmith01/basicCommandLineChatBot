"""
Functions needed for th eChat Bot to function

@author: bradleysmith
"""

#Import Modules
import os
import datetime

        
        
#Create Folder using OS Module
def createFolder(folderLocationSelection, folderName):
    """
    Creates a new folder in the user's storage.
    Parameters:
    folderLocationSelection : STR
        The File Path to the parent Folder.
    folderName : STR
        The Name of the New Folder.
    Returns:
    Print
    STR: A success or error message.
    """
    #Initialize As Empty
    folderLocation = ""

    if folderLocationSelection == "q" or folderLocationSelection == "quit":
        return
    elif folderLocationSelection == "1" or folderLocationSelection == "desktop":
        folderLocation = "/Users/bradleysmith/Desktop/"
    elif folderLocationSelection == "2" or folderLocationSelection == "downloads":
        folderLocation = "/Users/bradleysmith/Downloads/"
    elif folderLocationSelection == "3" or folderLocationSelection == "documents":
        folderLocation = "/Users/bradleysmith/Documents/"

    try:
        os.makedirs(folderLocation + folderName)
        print(f"Success:\nFolderName - {folderName},\nFolder - {folderLocation}")

    except:
        print("Error With Creating Folder")
            
    #Calculate Numer of Days between two Dates
def calcDateFromCurrent(fDateDay,fDateMonth,fDateYear,sDateDay,sDateMonth,sDateYear):
    """
    Calculates the differnce in days between two differnet dates

    Parameters
    ----------
    firstDate : TYPE
        DESCRIPTION.
    SecondDate : TYPE
        DESCRIPTION.

    Returns
    -------
    Print Statement.

    """
    firstDate = datetime.date(fDateYear,fDateMonth,fDateDay)
    secondDate = datetime.date(sDateYear,sDateMonth,sDateDay)
    delta = secondDate - firstDate
    #Strips chars out of output that arent needed for cleaner look
    deltaStr = str(delta)
    stripped_date = deltaStr.strip(", 0:00:00")
    print(stripped_date)

def percentChange(firstNumber,secondNumber):
    """
    To calculate the percent change

    Parameters
    ----------
    firstNumber : FLOAT
    
    secondNumber : FLOAT
 

    Returns
    -------
    Print Statment.

    """
    if firstNumber == "q" or secondNumber == "quit":
        return
    firstNumber = float(firstNumber)
    secondNumber = float(secondNumber)
    result = 0
    result = ((secondNumber - firstNumber) * 100) /firstNumber
    print(f"{result}%")
