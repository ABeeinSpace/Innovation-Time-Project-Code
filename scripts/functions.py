# Aidan Border and Jonas York
# CSC 1980 and CSC2280 LC3
# Innovation Time Project -- Helper File

# This file contains all of the Fun Functions that the main.py file needs in order to do its thing.

import os

def clear():
  """
  Function to define a way to clear the screen in a way that is cross-platform. I envision using it to improve readability once we show a guide or checklist by removing extraneous information from the screen.
  """

  if os.name == "nt":
    _ = os.system("cls")
  else:
    _ = os.system("clear")
def preflightChecks(droneManufacturer):
    """
    This function just grabs preflight checks from .txt files in the "checklists/preflight" folder under the same folder as the python files.
    """
    
    if droneManufacturer == "dji":
    # If the user has a DJI drone, then we try to load the preflight checklist specific to DJI drones. If we can't load it, we print a warning to the user stating that we could not find the file.
      try:
        textFileHandler = open(os.path.join("checklists", "preflight", "djiPreflight.txt"), "r")
        preflightList = textFileHandler.readlines()
        textFileHandler.close()
      except FileNotFoundError:
        print("The file djiPreflight.txt wasn't found! Please make sure the checklist folder is present in the same directory as this file!!")
      clear()
      print("".center(80, "-"))
      for each in preflightList: #type: ignore
        print(each)
      print()
      input("Press any key to continue...")
    if droneManufacturer == "parrot":
    # If the user has a Parrot drone, then we try to load the preflight checklist specific to Parrot drones. If we can't load it, we print a warning to the user stating that we could not find the file.
      try:
        textFileHandler = open("./checklists/preflight/parrrotPreflight.txt", "r")
        textFileHandler.close()
      except FileNotFoundError:
        print("ERROR: 'The file parrotPreflight.txt' wasn't found! Please make sure the checklist folder is present in the same directory as this file, or redownload this script.")

def takeoffChecklist(droneManufacturer):
    """
    This function grabs the takeoff checklists from text files located in "checklists/takeoff."
    """
    if droneManufacturer == "dji":
    # If the user has a DJI drone, then we try to load the takeoff checklist specific to DJI drones. If we can't load it, we print a warning to the user stating that we could not find the file.
      try:
        textFileHandler = open(os.path.join("checklists", "takeoff", "djiTakeoff.txt"), "r")
        takeoffList = textFileHandler.readlines()
        textFileHandler.close()
      except FileNotFoundError:
        print("The file wasn't found! Please make sure the checklist folder is present in the same directory as this file!!")
      clear()
      print("".center(80, "-"))
      for each in takeoffList: #type: ignore
        print(each)
      print()
      input("Press any key to continue...")
    if droneManufacturer == "parrot":
    # If the user has a Parrot drone, then we try to load the takeoff checklist specific to Parrot drones. If we can't load it, we print a warning to the user stating that we could not find the file.
      try:
        textFileHandler = open("./checklists/takeoff/parrrotTakeoff.txt", "r")
        textFileHandler.close()
      except FileNotFoundError:
        print("ERROR: 'The file parrotTakeoff.txt' wasn't found! Please make sure the checklist folder is present in the same directory as this file, or redownload this script.")


def flightChecklist(droneManufacturer):
    if droneManufacturer == "dji":
    # If the user has a DJI drone, then we try to load the flight checklist specific to DJI drones. If we can't load it, we print a warning to the user stating that we could not find the file.
      try:
        textFileHandler = open(os.path.join("checklists", "flight", "djiFlight.txt"), "r")
        preflightList = textFileHandler.readlines()
        textFileHandler.close()
      except FileNotFoundError:
        print("The file wasn't found! Please make sure the checklist folder is present in the same directory as this file!!")
      clear()
      print("".center(80, "-"))
      for each in preflightList: #type: ignore
        print(each)
      print()
      input("Press any key to continue...")
    if droneManufacturer == "parrot":
    # If the user has a Parrot drone, then we try to load the flight checklist specific to Parrot drones. If we can't load it, we print a warning to the user stating that we could not find the file.
      try:
        textFileHandler = open("./checklists/flight/parrrotFlight.txt", "r")
        textFileHandler.close()
      except FileNotFoundError:
        print("ERROR: 'The file parrotPreflight.txt' wasn't found! Please make sure the checklist folder is present in the same directory as this file, or redownload this script.")


def landingChecklist(droneManufacturer):
    if droneManufacturer == "dji":
    # If the user has a DJI drone, then we try to load the landing checklist specific to DJI drones. If we can't load it, we print a warning to the user stating that we could not find the file.
      try:
        textFileHandler = open(os.path.join("checklists", "landing", "djiLanding.txt"), "r")
        preflightList = textFileHandler.readlines()
        textFileHandler.close()
      except FileNotFoundError:
        print("The file wasn't found! Please make sure the checklist folder is present in the same directory as this file!!")
      clear()
      print("".center(80, "-"))
      for each in preflightList: #type: ignore
        print(each)
      print()
      input("Press any key to continue...")
    if droneManufacturer == "parrot":
    # If the user has a Parrot drone, then we try to load the preflight checklist specific to Parrot drones. If we can't load it, we print a warning to the user stating that we could not find the file.
      try:
        textFileHandler = open("./checklists/landing/parrrotLanding.txt", "r")
        textFileHandler.close()
      except FileNotFoundError:
        print("ERROR: 'The file parrotLanding.txt' wasn't found! Please make sure the checklist folder is present in the same directory as this file, or redownload this script.")



def displayMenu(droneManufacturer):
  """
  This function displays a menu that the user can pick options from. An invalid option is caught, we tell the user that they've picked an option that doesn't quite work and then loop back to the menu
  """
  userInput = ""
  clear()
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
      takeoffChecklist(droneManufacturer)
    elif userInput == "3":
      print("Accessing Flight Checklist...")
      flightChecklist(droneManufacturer)
    elif userInput == "4":
      print("Accessing Landing Checklist...")
      landingChecklist(droneManufacturer)
    elif userInput == "5":
      print("Accessing Non-Normal Checklist...")
      print("\033[31m" + "WARNING: Please only use these checklists for studying. If you actually have a flight that is going wrong, GET OFF YOUR COMPUTER NOW AND FLY THE DRONE".center(80) + "\033[39m")
      input("Press any key to ackknowledge this warning and continue....")
      displayNonNormalMenu()
    elif userInput == "6":
      print("Thank you for flying with us today!")
    else:
      print("Please input a valid menu option.")

def displayNonNormalMenu():
  """
  This function displays a menu of checklists for off-nominal conditions, such as a motor failure or loss of remote control signal.
  """
  print("Non-Normal Checklists".center(80,"-"))
  print("1) Motor Failure in Flight")
  print("2) Loss of Remote Control Signal in Flight")
  print("3) ")

def main():
  print("This is the main testing function from functions.py. It will print the paths of all checklist files and a warning if one wasn't found.")
  preflightPath = os.path.join("checklists", "preflight", "djiPreflight.txt")
  takeoffPath = os.path.join("checklists", "takeoff", "djiTakeoff.txt")
  flightPath = os.path.join("checklists", "flight", "djiFlight.txt")
  print(f"DJI Preflight Checklist: {str(os.path.exists(preflightPath))}")
  print(f"DJI Takeoff Checklist: {str(os.path.exists(takeoffPath))}")
  print(f"DJI Flight Checklist: {str(os.path.exists(flightPath))}")


if __name__ == "__main__":
    main()
