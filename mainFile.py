# Aidan Border and Jonas York
# CSC 1980 and CSC2280 LC3
# Innovation Time Project -- Main File

import functions

def main():
  """
  Main function for the program. It does all the things. Pretty kewl.
  """
  print
  # Adding a line so the user can specify which manufacturer their drone is from. This will matter for which checklists we surface to the user.
  droneManufacturer = input("Who made your drone? (Valid options are DJI and Parrot): ")
  if droneManufacturer != "DJI" or droneManufacturer != "Parrot":
    print("Sorry, we do not support specific checklists for your drone type yet. However, you may still be able to use some of the checklists.")
  
  functions.displayMenu(droneManufacturer)
  # print("yeet")
  # functions.printYeet()





if __name__ == "__main__":
    main()