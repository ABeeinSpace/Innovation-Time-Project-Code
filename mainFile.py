# Aidan Border and Jonas York
# CSC 1980 and CSC2280 LC3
# Innovation Time Project -- Main File

from scripts import functions, checklist

def main():
  """
  Main function for the program. It does all the things. Pretty kewl.
  """
  # Adding a line so the user can specify which manufacturer their drone is from. This will matter for which checklists we surface to the user.
  droneManufacturer = input("Who made your drone? (Valid options are DJI and Parrot): ").lower()
  print(droneManufacturer)
  if droneManufacturer == "dji":
    functions.displayMenu(droneManufacturer)
  elif droneManufacturer == "parrot":
    functions.displayMenu(droneManufacturer)
  else:
    print("Sorry, we do not support specific checklists for your drone type yet. However, you may still be able to use some of the checklists.")
    input("Press any key to continue....")
    functions.displayMenu(droneManufacturer)
  # print("yeet")
  # functions.printYeet()





if __name__ == "__main__":
    main()