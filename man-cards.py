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
ERROR_INPUT_OPTION = "ERROR: input is not available"

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
        try:
            for question, answer in data[category][module].items():
                cardbankQuestions.append(question)
                cardbankAnswers.append(answer)
            
            return(cardbankQuestions, cardbankAnswers)
        
        except KeyError:
            return KeyError
        
            


        
    ## first startup of program category should be empty                
    if (category == ""):
        return cardbankCategorys
    
    ## once category is chosen return the list of categorys in our cardbank.json
    elif (category):
        # print("category:", category)
        try:
            for i in data[category].items():
                cardbankModules.append(i[0]) 
            return cardbankModules
        except KeyError:
            return KeyError
       
        
    
    ## function that will prompt the user to load a question bank
def create_QA_bank(category="", module="", flag=""):
    # Create and prompt for category menu
    def main_menu_():

            


        main_menu_list = load_cards()
        print(main_menu_list)
        chosenCat = input("? Please choose an category: ")
    

        module_menu_list = load_cards(category=chosenCat)

        if module_menu_list == KeyError:
            print(ERROR_INPUT_OPTION)
            main_menu_()
        else:
            print(module_menu_list)
            module_menu_(chosenCat, input("? Please choose a module: "))

    def module_menu_(chosenCat, chosenMod):
    #load the chosen module into the global question and answer bank list
            loadedModuleBank = load_cards(category=chosenCat, module=chosenMod)
            if loadedModuleBank == KeyError:
                print(ERROR_INPUT_OPTION)
                module_menu_(chosenCat, input("? Please choose a module: "))
            else:
                return loadedModuleBank

    
    return main_menu_()
    


    # Create and prompt for module menu
    

"""


START OF PROGRAM


"""
QA_BANK = create_QA_bank()


print(QA_BANK)