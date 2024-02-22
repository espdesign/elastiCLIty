import json

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
    modulesList = []
    for i in chosenCategory.keys():
        modulesList.append(i)
    return modulesList

## return a dictonary of a specific category key
def load_chosen_category(arg):
    data = load_json()
    return data[arg]

## return the data of a chosen category & module 
def load_chosen_module(chosenCat, chosenMod):
    data = load_json()[chosenCat][chosenMod]
    return data


## main menu
def main_menu():
    print(list_categories())
    # chosen_category = load_category(input("Pick a category: "))

    chosenCategory = input("Pick a category: ")
    moduleList = list_modules(load_chosen_category(chosenCategory))
    # after picking category and loading list of modules start the module_menu
    return module_menu(moduleList, chosenCategory)
    

## module menu
def module_menu(moduleList, chosenCategory):
    print(moduleList)
    chosenModule = input("Pick a module: ")
    return load_chosen_module(chosenCategory, chosenModule)
    

##load the question and answer banks from chosen menu options
QA_DATA_BANK = main_menu()
QUESTION_BANK = []
ANSWER_BANK = []
for q, a in QA_DATA_BANK.items():
    QUESTION_BANK.append(q)
    ANSWER_BANK.append(a)

