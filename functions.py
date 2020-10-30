# Aidan Border
# CSC 1980 and CSC2280 LC3
# Innovation Time Project -- Helper File

# This file contains all of the Fun Functions that the main.py file needs in order to do its thing.

import mainFile

def displayMenu(droneManufacturer):
  """
  This function displays a menu that the user can pick options from
  """
  userInput = ""
  while userInput != "6":
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
      
    elif userInput == "2":
      print("Accessing Takeoff Checklist...")
    elif userInput == "3":
      print("Accessing Flight Checklist...")
    elif userInput == "4":
      print("Accessing Landing Checklist...")
    elif userInput == "5":
      print("Accessing Non-normal Checklist...")
    elif userInput == "6":
      print("Thank you for flying with us today!")
    else:
      print("Please input a valid menu option.")


  def preflightChecks(droneManufacturer):
    """
    This function just grabs preflight checks from .txt files in the "checklists" folder under same folder as the python files.
    """
    
    while True:
      try:
        textFileHandler = open("./checklists/preflight")
      except fileNotFoundError:
        print()
        


# def printYeet():
#   """
#   docstring
#   """
#   print("double yeet.")
