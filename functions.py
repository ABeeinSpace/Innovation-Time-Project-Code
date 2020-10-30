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
  while userInput != "4":
    print("GIVE ME A TITLE".center(80,"-"))
    print()
    print("1) Menu Option 1")
    print("2) Menu Option 2")
    print("3) Menu Option 3")
    print("4) Exit")
    userInput = input("Type which option you wish to run here: ")
    if userInput == "1":
      print("You picked option 1!")
    elif userInput == "2":
      print("You picked option 2!")
    elif userInput == "3":
      print("You picked option 3!")
    elif userInput == "4":
      print("Have a nice rest of your day!".center(80))
    else:
      print("Please input a valid menu option")


  


def printYeet():
  """
  docstring
  """
  print("double yeet.")
