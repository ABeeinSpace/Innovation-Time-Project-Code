# Aidan Border
# CSC 1980 and CSC2280 LC3
# Innovation Time Project -- Helper File

# This file contains all of the Fun Functions that the main.py file needs in order to do its thing.

import mainFile

def preflightChecks(droneManufacturer):
    """
    This function just grabs preflight checks from .txt files in the "checklists" folder under same folder as the python files.
    """
    
    if droneManufacturer == "DJI":
      try:
        textFileHandler = open("./checklists/preflight/djiPreflight/txt", "r")
        textFileHandler.close()
      except:
        print("The file wasn't found! Please make sure the checklist folder is present in the same directory as this file!!!")

def takeoffChecklist(droneManufacturer):
    """
    docstring
    """
    print("Do stuff and things")

def displayMenu(droneManufacturer):
  """
  This function displays a menu that the user can pick options from
  """
  userOption = ""
  while userOption != "6":
    print("Please Choose Your Stage of Flight.".center(80,"-"))
    print()
    print("1) Preflight")
    print("2) Takeoff")
    print("3) Flight")
    print("4) Landing")
    print("5) Non-normal Checklist")
    print("6) Exit")
    userOption = input("Type which option you wish to run here: ")
    if userOption == "1":
      preflightChecks(droneManufacturer)
    elif userOption == "2":
      print("You picked option 2!")
    elif userOption == "3":
      print("You picked option 3!")
    elif userOption == "4":
      print("You picked option 4!")
    elif userOption == "5":
      print("You picked option 5!")
    elif userOption == "6":
      print("Thank you for flying with us today!")
    else:
      print("Please input a valid menu option")


# def printYeet():
#   """
#   docstring
#   """
#   print("double yeet.")
