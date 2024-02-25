import json
import random

"""
########################
    START OF 
    MENU SYSTEM
#######################
"""
## Load data from file
cls = lambda: print('\n'*100)
def load_json():
    f = open('cardbank.json')
    data = json.load(f)
    f.close()
    return data


## List the categories from the cardbank.json file
def list_categories():
    categories = []
    for i in load_json().keys():
        categories.append(i)
    return categories

## List the modules from the chosenCategory listed in cardbank.json file
def list_modules(chosenCategory):
    if chosenCategory == None:
        return None
    else: 
        modulesList = []
        for i in chosenCategory.keys():
            modulesList.append(i)
        return modulesList

## return a dictonary of a specific category key
def load_chosen_category(arg):
    data = load_json()
    try:
        data[arg]
    except KeyError:
        cls()
        print("load_chosen_category: KeyError:")
        return None
    else:
        return data[arg]

## return the data of a chosen category & module 
def load_chosen_module(chosenCatDict, ChosenModule):

    try:
        chosenCatDict[ChosenModule]
    except KeyError:
        cls()
        print("load_chosen_module: KeyError:")
        return None
    else:
        return chosenCatDict[ChosenModule]


## Handle key errors: input
def category_input_checker():
    print(list_categories())
    chosenCategory = load_chosen_category(input("Pick a category: "))
    ## CHECK FOR KEY ERRORSS
    if chosenCategory == None:
        print("No category found with that name please try again. (case sensitive)")
        main_menu()
        
    else:
        return(chosenCategory)

## Handle key errors: input
def module_input_checker(chosenCategory):
    print(list_modules(chosenCategory))
    chosenModule = load_chosen_module(chosenCategory, input("Pick a module: "))

    if chosenModule == None:
        print("No module found with that name please try again. (case sensitive)")
        module_menu(chosenCategory)
    else:
        return chosenModule


## main menu
def main_menu():
    cls()
    ## pick a category and check to see if category exists.
    chosenCategory = category_input_checker()
    ## load the modules from the chosen category
    module_menu(chosenCategory)


## seccondary module menu
def module_menu(chosenCategory):
    cls()
    ## pick a module, check to see if module exists
    chosenModule = module_input_checker(chosenCategory)
    ## load the modules into the databank of questions:answers
    data_bank_builder(chosenModule)


"""
############################
    DATABANK LOGIC
    BUILD THE QUESTION 
    AND ANSWER BANKS
############################
"""

#load the question and answer banks from chosen menu options
def data_bank_builder(chosenModule):
    QA_DATA_BANK = chosenModule
    QUESTION_BANK = []
    ANSWER_BANK = []
    for q, a in QA_DATA_BANK.items():
        QUESTION_BANK.append(q)
        ANSWER_BANK.append(a)

    ## send the QUESTION AND ANSWER BANK's to the game logic
    game(QUESTION_BANK,ANSWER_BANK)

"""
########################
    START OF 
    GAME SYSTEM
#######################
"""


## main game logic
def game(QUESTION_BANK, ANSWER_BANK):

    ### a sudo clear screen to print 100 new lines
    
        
    ## Return a random index from the QUESTION_BANK
    def random_question_index():
        QUESTION_BANK_indexLength = len(QUESTION_BANK) - 1
        return random.randint(0, QUESTION_BANK_indexLength)
    
    ## return a answer key from a designated index
    def load_answer_from_index(index):
        answerAtIndex = ANSWER_BANK[index]
        return answerAtIndex
    ## return a question from a designated index
    def load_question_from_index(index):
        questionAtIndex = QUESTION_BANK[index]
        return questionAtIndex

    ## print a question and return questions index
    def print_question_return_index():
        index = random_question_index()
        print(QUESTION_BANK[index], end="")
        return index
    
    ## prompt the player for a answer and return the input
    def prompt_for_answer_return_input():
        player_answer = input(": $ ")
        return player_answer
    
    ## check if answer is correct using the player input and an the answer key from an index
    def check_answer_is_correct(player_input, index):
        if player_input == load_answer_from_index(index):
            return True
        else:
            return False

    """
    ########################
    MAIN QUESTION
    LOOP LOGIC
    #######################
    """

    def answer_is_bool_logic(bool, index):
        if bool == True:
            # print(f"CORRECT!")
            display = "CORRECT: Next Question..."
            question_logic(display)
        else:
            display = f"WRONG: The correct answer is: {load_answer_from_index(index)}"
            # print(f"WRONG: \n The correct answer is:", load_answer_from_index(index))
            initalize_same_question(index, display)

    def question_logic(display):
        cls()
        print(display)
        index = print_question_return_index()
        grab_player_answer_true_or_false(index)

  
    def initalize_same_question(index, display):
        cls()
        print(display)
        print(load_question_from_index(index), end = "")
        grab_player_answer_true_or_false(index)

    def grab_player_answer_true_or_false(index):
        player_answer = prompt_for_answer_return_input()
        bool = check_answer_is_correct(player_answer, index)
        answer_is_bool_logic(bool, index)

    
    
    """
    #########################################
        INIT FIRST QUESTION
    #########################################
    """

    question_logic(display = "")

"""
#########################################
    INIT START OF PROGRAM AND MAIN MENU
#########################################
"""

main_menu()