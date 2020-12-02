# Aidan Border and Jonas York
# CSC 1980 and CSC2280 LC3
# Innovation Time Project -- Main File

# This boi handles initialization and asks the user for their drone manufacturer. After it gets that thing from the user, it gets saved to the droneManufacturer variable. That variable gets passed into displayMenu() so I can surface the correct guides and checklists. For right now, it looks like I'll only end up having one manufacturer, DJI. More could be added at a later date.

from scripts import functions, checklist

def main():
  """
  This function sets up everything that the functions.py file needs, and then passes control to the displayMenu() function inside of functions.py.
  """
  # Adding a line so the user can specify which manufacturer their drone is from. This will matter for which checklists we surface to the user.
  droneManufacturer = input("Who made your drone? (Valid options are DJI and Parrot): ").lower()
  if droneManufacturer == "dji":
    functions.displayMenu(droneManufacturer)
  elif droneManufacturer == "parrot":
    functions.displayMenu(droneManufacturer)
  else:
    print("Sorry, we do not support specific checklists for your drone type yet. However, you may still be able to use some of the checklists.")
    input("Press Enter to continue....")
    functions.displayMenu(droneManufacturer)

if __name__ == "__main__":
    main()