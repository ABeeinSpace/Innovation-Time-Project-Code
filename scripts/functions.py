# Aidan Border and Jonas York
# CSC 1980 and CSC2280 LC3
# Innovation Time Project -- Helper File

# This file contains all of the Fun Functions that the main.py file needs in order to do its thing.

import os, textwrap

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
    # If the user has a DJI drone, then we try to load the preflight checklist specific to DJI drones. If we can't load it, we print a warning to the user stating that we could not find the file and then exit so we dont crash.
    try:
      textFileHandler = open(os.path.join("checklists", "preflight", "djiPreflight.txt"), "r")
      preflightList = textFileHandler.readlines()
      textFileHandler.close()
    except FileNotFoundError:
      print("\033[31m" + "The file djiPreflight.txt wasn't found! Please make sure the checklist folder is present in the same directory as this file!!" + "\033[39m")
      return
    clear()
    print("".center(80, "-"))
    for each in preflightList: #type: ignore
      print(textwrap.fill(each, width=80))
      print()
    print()
    input("Press Enter to continue...")
  # if droneManufacturer == "parrot":
  # # If the user has a Parrot drone, then we try to load the preflight checklist specific to Parrot drones. If we can't load it, we print a warning to the user stating that we could not find the file.
  #   try:
  #     textFileHandler = open("./checklists/preflight/parrrotPreflight.txt", "r")
  #     textFileHandler.close()
  #   except FileNotFoundError:
  #     print("ERROR: 'The file parrotPreflight.txt' wasn't found! Please make sure the checklist folder is present in the same directory as this file, or redownload this script.")

def takeoffChecklist(droneManufacturer):
    """
    This function grabs the takeoff checklists from text files located in "checklists/takeoff."
    """
    # If the user has a DJI drone, then we try to load the takeoff checklist specific to DJI drones. If we can't load it, we print a warning to the user stating that we could not find the file, and then exit so we dont crash.
    try:
      textFileHandler = open(os.path.join("checklists", "takeoff", "djiTakeoff.txt"), "r")
      takeoffList = textFileHandler.readlines()
      textFileHandler.close()
    except FileNotFoundError:
      print("\033[31m" + "The file djiPreflight.txt wasn't found! Please make sure the checklist folder is present in the same directory as this file!!" + "\033[39m")
      return
    clear()
    print("".center(80, "-"))
    for each in takeoffList: #type: ignore
      print(textwrap.fill(each, width=80))
      print()
    print()
    input("Press Enter to continue...")
  # if droneManufacturer == "parrot":
  # # If the user has a Parrot drone, then we try to load the takeoff checklist specific to Parrot drones. If we can't load it, we print a warning to the user stating that we could not find the file and then exit.
  #   try:
  #     textFileHandler = open("./checklists/takeoff/parrrotTakeoff.txt", "r")
  #     textFileHandler.close()
  #     return
  #   except FileNotFoundError:
  #     print("ERROR: 'The file parrotTakeoff.txt' wasn't found! Please make sure the checklist folder is present in the same directory as this file, or redownload this script.")


def flightChecklist(droneManufacturer):
  """
  This function grabs the flight checklists from text files located in "checklists/flight."
  """

  # If the user has a DJI drone, then we try to load the flight checklist specific to DJI drones. If we can't load it, we print a warning to the user stating that we could not find the file, and then exit so we dont crash.
  try:
    textFileHandler = open(os.path.join("checklists", "flight", "djiFlight.txt"), "r")
    preflightList = textFileHandler.readlines()
    textFileHandler.close()
  except FileNotFoundError:
    print("\033[31m" + "The file djiPreflight.txt wasn't found! Please make sure the checklist folder is present in the same directory as this file!!" + "\033[39m")
    return
  clear()
  print("".center(80, "-"))
  for each in preflightList: #type: ignore
    print(textwrap.fill(each, width=80))
    print()
  print()
  input("Press Enter to continue...")
# if droneManufacturer == "parrot":
# # If the user has a Parrot drone, then we try to load the flight checklist specific to Parrot drones. If we can't load it, we print a warning to the user stating that we could not find the file and then exit.
#   try:
#     textFileHandler = open("./checklists/flight/parrrotFlight.txt", "r")
#     textFileHandler.close()
#   except FileNotFoundError:
#     print("ERROR: The file 'parrotPreflight.txt' wasn't found! Please make sure the checklist folder is present in the same directory as this file, or redownload this script.")



def landingChecklist(droneManufacturer):
  """
  This function grabs the takeoff checklists from text files located in "checklists/takeoff."
  """
  # If the user has a DJI drone, then we try to load the landing checklist specific to DJI drones. If we can't load it, we print a warning to the user stating that we could not find the file.
  try:
    textFileHandler = open(os.path.join("checklists", "landing", "djiLanding.txt"), "r")
    preflightList = textFileHandler.readlines()
    textFileHandler.close()
  except FileNotFoundError:
    print("\033[31m" + "The file djiPreflight.txt wasn't found! Please make sure the checklist folder is present in the same directory as this file!!" + "\033[39m")
    return
  clear()
  print("".center(80, "-"))
  for each in preflightList: #type: ignore
    print(textwrap.fill(each, width=80))
    print() 
  print()
  input("Press Enter to continue...")
# if droneManufacturer == "parrot":
# # If the user has a Parrot drone, then we try to load the preflight checklist specific to Parrot drones. If we can't load it, we print a warning to the user stating that we could not find the file.
#   try:
#     textFileHandler = open("./checklists/landing/parrrotLanding.txt", "r")
#     textFileHandler.close()
#   except FileNotFoundError:
#     print("ERROR: 'The file parrotLanding.txt' wasn't found! Please make sure the checklist folder is present in the same directory as this file, or redownload this script.")
#     return



def displayMenu(droneManufacturer):
  """
  This function displays a menu that the user can pick options from. An invalid option is caught, we tell the user that they've picked an option that doesn't quite work and then loop back to the menu
  """
  userInput = ""
  while userInput != "6":
    clear()
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
      input("Press Enter to ackknowledge this warning and continue....")
      displayNonNormalMenu(droneManufacturer)
    elif userInput == "6":
      print("Thank you for flying with us today!")
    else:
      print("\033[31m" + "Please input a valid menu option." + "\033[39m")

def displayNonNormalMenu(droneManufacturer):
  """
  This function displays a menu of checklists for off-nominal conditions, such as a motor failure or loss of remote control signal.
  """
  userInput = ""
  clear()
  while userInput != "4":
    print("Non-Normal Checklists".center(80,"-"))
    print()
    print("1) Motor Failure in Flight")
    print("2) Loss of Remote Control Signal in Flight")
    print("3) Gimbal Overload Error prior to takeoff or in flight")
    print("4) Back to Main Menu")
    userInput = input("Type which option you wish to run here: ")
    if userInput == "1":
      print("Accessing Motor Failure Checklist...")
      motorFailureAccessor()
    elif userInput == "2":
      print("Accessing LOS Checklist...")
      lossOfSignalAccessor()
    elif userInput == "3":
      print("Accessing Gimbal Overload Checklist...")
      GimbalOverloadAccessor()
    elif userInput == "4":
      return
    else:
      print("\033[31m" + "Please input a valid menu option." + "\033[39m")

def motorFailureAccessor():
  """
  Accessor method for the motor failure *shudder* checklist. For all the drone pilots out there, I hope that you never have to use the items in this checklist, I really do. Motor failure at altitude means a Not Fun Repair Bill
  """
  try:
    textFileHandler = open(os.path.join("checklists", "non-normal",  "djiMotorFailure.txt"), "r")
    motorFailureList = textFileHandler.readlines()
    textFileHandler.close()
  except FileNotFoundError:
    print("\033[31m" + "The file djiPreflight.txt wasn't found! Please make sure the checklist folder is present in the same directory as this file!!" + "\033[39m")
    return
  clear()
  print("".center(80, "-"))
  for each in motorFailureList: #type: ignore
    print(textwrap.fill(each, width=80))
    print()
  print()
  input("Press Enter to continue...")

def lossOfSignalAccessor():
  """
  Accessor method for the Loss of RC Signal checklist
  """
  try:
    textFileHandler = open(os.path.join("checklists", "non-normal",  "djiLossOfRCSignal.txt"), "r")
    losList = textFileHandler.readlines()
    textFileHandler.close()
  except FileNotFoundError:
    print("\033[31m" + "The file djiPreflight.txt wasn't found! Please make sure the checklist folder is present in the same directory as this file!!" + "\033[39m")
    return
  clear()
  print("".center(80, "-"))
  for each in losList: #type: ignore
    print(textwrap.fill(each, width=80))
    print()
  print()
  input("Press Enter to continue...")

def GimbalOverloadAccessor():
  """
  Accessor method for the loss of signal checklist
  """
  try:
    textFileHandler = open(os.path.join("checklists", "non-normal",  "djiGimbalOverload.txt"), "r")
    gimbalOverloadList = textFileHandler.readlines()
    textFileHandler.close()
  except FileNotFoundError:
    print("\033[31m" + "The file djiPreflight.txt wasn't found! Please make sure the checklist folder is present in the same directory as this file!!" + "\033[39m")
    return
  clear()
  print("".center(80, "-"))
  for each in gimbalOverloadList: #type: ignore
    print(textwrap.fill(each, width=80))
    print()
  print()
  input("Press Enter to continue...")

def main():
  print("This is a diagnostic function. It will print the paths of all checklist files and a warning if one wasn't found. If that warning gets printed, please check that the affected file is in the expected location. If the file is in the correct location and a warning is still thrown, please redownload the program from my GitHub repository")
  preflightPath = os.path.join("checklists", "preflight", "djiPreflight.txt")
  takeoffPath = os.path.join("checklists", "takeoff", "djiTakeoff.txt")
  flightPath = os.path.join("checklists", "flight", "djiFlight.txt")
  landingPath = os.path.join("checklists", "landing", "djiLanding.txt")
  gimbalOverloadPath = os.path.join("checklists", "non-normal", "djiGimbalOverload.txt")
  lossOfRCPath = os.path.join("checklists", "non-normal", "djiLossOfRCSignal.txt")
  motorFailurePath = os.path.join("checklists", "non-normal", "djiMotorFailure.txt")
  print(f"DJI Preflight Checklist: {str(os.path.exists(preflightPath))}")
  print(f"DJI Takeoff Checklist: {str(os.path.exists(takeoffPath))}")
  print(f"DJI Flight Checklist: {str(os.path.exists(flightPath))}")
  print(f"DJI Landing Checklist: {str(os.path.exists(landingPath))}")
  print(f"Gimbal Overload Checklist: {str(os.path.exists(gimbalOverloadPath))}")
  print(f"Loss of RC Signal Checklist: {str(os.path.exists(lossOfRCPath))}")
  print(f"Motor Failure Checklist: {str(os.path.exists(motorFailurePath))}")


if __name__ == "__main__":
    main()
