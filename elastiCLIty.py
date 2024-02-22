import json
import random


QA_DATA_BANK = []

## Load data from file
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
        print("load_chosen_category: Key Error:")
        return None
    else:
        return data[arg]

## return the data of a chosen category & module 
def load_chosen_module(chosenCatDict, ChosenModule):

    try:
        chosenCatDict[ChosenModule]
    except KeyError:
        print("Load_chosen_module: KeyError")
        return None
    else:
        return chosenCatDict[ChosenModule]


## Handle key errors: input
def category_input_checker():
    print(list_categories())
    chosenCategory = load_chosen_category(input("Pick a category: "))
    ## CHECK FOR KEY ERRORSS
    if chosenCategory == None:
        print("No category found with that name please try again.")
        main_menu()
        
    else:
        return(chosenCategory)

## Handle key errors: input
def module_input_checker(chosenCategory):
    print(list_modules(chosenCategory))
    chosenModule = load_chosen_module(chosenCategory, input("Pick a module: "))

    if chosenModule == None:
        print("No module found with that name please try again.")
        module_menu(chosenCategory)
    else:
        return chosenModule


## main menu
def main_menu():
    chosenCategory = category_input_checker()
    module_menu(chosenCategory)


## seccondary module menu
def module_menu(chosenCategory):
    chosenModule = module_input_checker(chosenCategory)
    data_bank_builder(chosenModule)



#load the question and answer banks from chosen menu options
def data_bank_builder(chosenModule):
    QA_DATA_BANK = chosenModule
    QUESTION_BANK = []
    ANSWER_BANK = []
    for q, a in QA_DATA_BANK.items():
        QUESTION_BANK.append(q)
        ANSWER_BANK.append(a)
    game(QUESTION_BANK,ANSWER_BANK)


def game(QUESTION_BANK, ANSWER_BANK):
    cls = lambda: print('\n'*100)
    indexLength = len(QUESTION_BANK) - 1
    randQuestionIndex = random.randint(0, indexLength)
    correct_answer = ANSWER_BANK[randQuestionIndex]
    player_answer = input(f"{QUESTION_BANK[randQuestionIndex]}? : $ ")

    if player_answer == correct_answer:
        cls()
        print("Correct!")

    else:
        print(f"Incorrect, the answer is: {correct_answer}")

    game(QUESTION_BANK, ANSWER_BANK)



main_menu()