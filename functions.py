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
    userInput = input("Type which option you wish to run here: ")
    if userInput == "1":
      print("Accessing Preflight Checklist...")
      checklists.preflight()
    elif userInput == "2":
      print("Accessing Takeoff Checklist...")
      checklists.takeoff()
    elif userInput == "3":
      print("Accessing Flight Checklist...")
      checklists.flight()
    elif userInput == "4":
      print("Accessing Landing Checklist...")
      checklists.landing()
    elif userInput == "5":
      print("Accessing Non-normal Checklist...")
      checklists.non-normal()
    elif userInput == "6":
      print("Thank you for flying with us today!")
    else:
      print("Please input a valid menu option.")


# def printYeet():
#   """
#   docstring
#   """
#   print("double yeet.")
