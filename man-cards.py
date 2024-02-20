# Declare global Menu Dictionarys 
MENU_DICT = [
    # MENU_DICT[0] == Menu Title
    {0: 'Main Menu', 1: 'Linux Basics.',2: 'Git.', 3: 'Grep', 4: 'Ports'},
    {0: 'Linux Basics,', 1: 'Linux Level One', 2: 'Linux Level Two', 3: 'Linux Level Three.'},
    {0: 'Git', 1: 'Git Level One', 2: 'Git Level Two', 3: 'Git Level Three.'},
    {0: 'Grep', 1: 'Grep Level One', 2: 'Grep Level Two', 3: 'Grep Level Three.'},
    {0: 'Ports', 1: 'Ports Level One', 2: 'Ports Level Two', 3: 'Ports Level Three.'}
    ]


#Iterate over the chosen menu and render it out
def render_menu(menuID):
    for x in MENU_DICT[menuID]:
        ## the menu title is always key 0
        if x == 0:
            print(MENU_DICT[menuID][x])
        ## if not menu title, first key, print the option and option string
        else:
            print(x, MENU_DICT[menuID][x])
    # if not main menu print return option
    if menuID != 0:
        print("0 Return to main menu")

    # prompt for menu option choice  
    optionID = int(input("Pick an Option: "))
    while optionID not in MENU_DICT[menuID]:
        optionID = int(input("Pick a better Option: "))
    menu_choice(menuID, optionID)
    # optionID = int(input("Pick an Option: "))

    # while optionID not in MENU_DICT[menuID]:
    #     invalid_option(menuID, optionID)

    # menu_choice(menuID, optionID)

  
def invalid_option(menuID, optionID):
    input("Sorry {} is not a valid menu option.\npress enter to continue...".format(optionID))
    render_menu(menuID)

#process menu chosen menu option
def menu_choice(menuID, optionID):
    loadMenuID = optionID
    # print(f"Loading {MENU_DICT[menuID][optionID]}")
    # current_menu = MENU_DICT[menuID][optionID]
    render_menu(loadMenuID)

# Start the main menu render
print("man Cards -- learn linux with CLI flashcards")
render_menu(0)






# def menu_error(menuID, optionID):
#     input("Sorry {} is not a valid option, press enter to continue...".format(optionID))
#     menu_return(menuID)
