# Aidan Border
# CSC 1980 and CSC2280 LC3
# Innovation Time Project -- Helper File

# This file contains all of the Fun Functions that the main.py file needs in order to do its thing.

import mainFile

def displayMenu(droneManufacturer):
  """
  This function displays a menu that the user can pick options from
  """
  userOption = ""
  while userOption != "4":
    print("GIVE ME A TITLE".center(80,"-"))
    print()
    print("1) Menu Option 1")
    print("2) Menu Option 2")
    print("3) Menu Option 3")
    print("4) Exit")
    userOption = input("Type which option you wish to run here: ")
    if userOption == "1":
      preflightChecks
    elif userOption == "2":
      print("You picked option 2!")
    elif userOption == "3":
      print("You picked option 3!")
    elif userOption == "4":
      print("Have a nice rest of your day!".center(80))
    else:
      print("Please input a valid menu option")


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
