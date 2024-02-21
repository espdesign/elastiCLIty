# import json

# def loadcards(category, module):
#     f = open('cards.json')
#     data = json.load(f)
#     f.close()
 
#     for i in data[category]:
#         print(i)

#     return(data[category][module])

# loadcards("Linux", "0")

import json

QA_BANK = []

"""

Load from cardbank.json

"""

def load_cards(category="", module="", flag=""):
    f = open('cardbank.json')
    data = json.load(f)
    f.close()

    # define data return variables
    cardbankQuestions = []
    cardbankAnswers = []
    cardbankCategorys = []
    cardbankModules = []

    ## First find categorys available
    for i in data.items():
        cardbankCategorys.append(i[0])

    ## Check for options, if no options exist. return the categorys.
        
    ## First check if module was chosen, if null then skip over and check for category
    if (module):
        for question, answer in data[category][module].items():
            cardbankQuestions.append(question)
            cardbankAnswers.append(answer)
        return(cardbankQuestions, cardbankAnswers)
    ## first startup of program category should be empty                
    if (category == ""):
        return cardbankCategorys
    
    ## once category is chosen return the list of categorys in our cardbank.json
    elif (category):
        # print("category:", category)
        for i in data[category].items():
            cardbankModules.append(i[0])
        return cardbankModules
    
    ## function that will prompt the user to load a question bank
def create_QA_bank(category="", module="", flag=""):
    # Create and prompt for category menu
    menu = load_cards()
    print(menu)
    chosenOptionCategory = input("? Please choose an option: ")
    # Create and prompt for module menu
    menu = load_cards(category=chosenOptionCategory)
    print(menu)
    chosenOptionModule = input("? Please choose an option: ")

    #load the chosen module into the global question and answer bank list
    loadedModuleBank = load_cards(category=chosenOptionCategory, module=chosenOptionModule)
    return loadedModuleBank

"""


START OF PROGRAM


"""
QA_BANK = create_QA_bank()




print(QA_BANK)