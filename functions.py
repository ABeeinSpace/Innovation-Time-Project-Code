# Aidan Border
# CSC 1980 and CSC2280 LC3
# Innovation Time Project -- Helper File

# This file contains all of the Fun Functions that the main.py file needs in order to do its thing.

import mainFile

def displayMenu():
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
      print("You picked option 1!")
    elif userInput == "2":
      print("You picked option 2!")
    elif userInput == "3":
      print("You picked option 3!")
    elif userInput == "4":
      print("You picked option 4!")
    elif userInput == "5":
      print("You picked option 5!")
    elif userInput == "6":
      print("Thank you for flying with us today!")
    else:
      print("Please input a valid menu option")


def printYeet():
  """
  docstring
  """
  print("double yeet.")
