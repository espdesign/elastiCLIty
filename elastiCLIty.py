import json
import random


"""
########################
    START OF 
    MENU SYSTEM
#######################
"""
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
        print("load_chosen_category: KeyError:")
        return None
    else:
        return data[arg]

## return the data of a chosen category & module 
def load_chosen_module(chosenCatDict, ChosenModule):

    try:
        chosenCatDict[ChosenModule]
    except KeyError:
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
    chosenCategory = category_input_checker()
    module_menu(chosenCategory)


## seccondary module menu
def module_menu(chosenCategory):
    chosenModule = module_input_checker(chosenCategory)
    data_bank_builder(chosenModule)


"""
########################
    START OF 
    GAME SYSTEM
#######################
"""

#load the question and answer banks from chosen menu options
def data_bank_builder(chosenModule):
    QA_DATA_BANK = chosenModule
    QUESTION_BANK = []
    ANSWER_BANK = []
    for q, a in QA_DATA_BANK.items():
        QUESTION_BANK.append(q)
        ANSWER_BANK.append(a)
    game(QUESTION_BANK,ANSWER_BANK)


## main game logic
def game(QUESTION_BANK, ANSWER_BANK):

    cls = lambda: print('\n'*100)
        

    def random_question_index():
        QUESTION_BANK_indexLength = len(QUESTION_BANK) - 1
        return random.randint(0, QUESTION_BANK_indexLength)
    
    def load_question_from_random_index():
        index = random_question_index()
        question = QUESTION_BANK[index]
        return question, index

    def load_question_answer_from_index(index):
        answerAtIndex = ANSWER_BANK[index]
        return answerAtIndex
    
    def load_question_from_index(index):
        questionAtIndex = QUESTION_BANK[index]
        return questionAtIndex

    def print_question():
        question, index = load_question_from_random_index()
        # print(f"question is: {question}, index is {index}")
        print(QUESTION_BANK[index])
        return question, index
    
    def print_answer(index):
        print(ANSWER_BANK[index])
        return

    def prompt_for_answer():
        player_answer = input("$ ")
        return player_answer
    

    def check_answer_is_correct(player_answer, index_of_correct_answer):
        correct_answer = load_question_answer_from_index(index_of_correct_answer)
        if player_answer == correct_answer:
            return True
        else:
            return False

    ## Clear Screen
    def game_question_loop():
        
        def first_question_init():
            cls()

            question, index = print_question()
            player_answer = prompt_for_answer()

            bool = check_answer_is_correct(player_answer, index)
            
            question_next_logic(bool, index)

        def question_next_logic(bool, index):
            if bool == True:
                print(f"CORRECT!")
                initalize_new_question()
            else:
                print(f"WRONG: \n The correct answer is:", load_question_answer_from_index(index))
                
                initalize_same_question(index)
            

        def initalize_new_question():
            first_question_init()
        
        def initalize_same_question(index):
            print(load_question_from_index(index))
            player_answer = prompt_for_answer()
            bool = check_answer_is_correct(player_answer, index)
            question_next_logic(bool, index)



        first_question_init()

    game_question_loop()
    
## Start Main Game Loop    
    game(QUESTION_BANK, ANSWER_BANK)


## Start MAIN MENU
main_menu()