# Aidan Border and Jonas York
# CSC 1980 and CSC2280 LC3
# Innovation Time Project -- Helper File

# This file contains all of the Fun Functions that the main.py file needs in order to do its thing.

import mainFile
import os


def clear():
  if os.name == "nt":
    _ = os.system("cls")
  else:
    _ = os.system("clear")
def preflightChecks(droneManufacturer):
    """
    This function just grabs preflight checks from .txt files in the "checklists" folder under the same folder as the python files.
    """
    
    if droneManufacturer == "dji":
    # If the user has a DJI drone, then we try to load the preflight checklist specific to DJI drones. If we can't load it, we print a warning to the user stating that we could not find the file.
      try:
        textFileHandler = open(os.path.join("checklists", "preflight", "djiPreflight.rtf"), "r")
        textFileHandler.close()
      except FileNotFoundError:
        print("The file wasn't found! Please make sure the checklist folder is present in the same directory as this file!!!")
    if droneManufacturer == "parrot":
    # If the user has a Parrot drone, then we try to load the preflight checklist specific to Parrot drones. If we can't load it, we print a warning to the user stating that we could not find the file.
      try:
        textFileHandler = open("./checklists/preflight/parrrotPreflight.txt", "r")
        textFileHandler.close()
      except FileNotFoundError:
        print("ERROR: 'The file djiPreflight.txt' wasn't found! Please make sure the checklist folder is present in the same directory as this file, or redownload this script.")

def takeoffChecklist(droneManufacturer):
    """
    docstring
    """
    print("Add things here!!!")

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
      preflightChecks(droneManufacturer)
    elif userInput == "2":
      print("Accessing Takeoff Checklist...")
      # checklists.takeoff()
    elif userInput == "3":
      print("Accessing Flight Checklist...")
      # checklists.flight()
    elif userInput == "4":
      print("Accessing Landing Checklist...")
      # checklists.landing()
    elif userInput == "5":
      print("Accessing Non-Normal Checklist...")
      print("\033[31m" + "WARNING: Please only use these checklists for studying. If you actually have a flight that is going wrong, GET OFF YOUR COMPUTER NOW AND FLY THE DRONE".center(80) + "\033[39m")
      input("Press any key to continue....")
      # checklists.non-normal()
    elif userInput == "6":
      print("Thank you for flying with us today!")
    else:
      print("Please input a valid menu option.")


# def printYeet():
#   """
#   docstring
#   """
#   print("double yeet.")
