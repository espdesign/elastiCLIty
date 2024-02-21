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
    if (module):
        for question, answer in data[category][module].items():
            cardbankQuestions.append(question)
            cardbankAnswers.append(answer)
        return(cardbankQuestions, cardbankAnswers)
                    
    if (category == ""): # and (module == "") and (flag == ""):
        return cardbankCategorys
    elif (category):
        # print("category:", category)
        for i in data[category].items():
            cardbankModules.append(i[0])
        return cardbankModules
    


    # for i in data[category].items():
    #     # print(i[0])
    #     cardbankModules.append(i[0])

    # for question, answer in data[category][module].items():

    #     cardbankQuestions.append(question)
    #     cardbankAnswers.append(answer)

    #     # print(question, answer)
    #     # print(f"The question: {question} \n The answer: {answer}")
    
    
    # if flag == "q":
    #     return(cardbankQuestions)
    # if flag == "a":
    #     return(cardbankAnswers)
    # if flag == "c":
    #     return(cardbankCategorys)
    


    # cardbank = data[category][module].items()
    # print(cardbank)
    # return(cardbank)

# card = load_cards("Linux", "Module 0", "c")

def create_question_bank(category="", module="", flag=""):
    menu = load_cards()

    print(menu)
    chosenOptionCategory = input("? Please choose an option: ")

    menu = load_cards(category=chosenOptionCategory)

    print(menu)
    chosenOptionModule = input("? Please choose an option: ")

    loadedModuleBank = load_cards(category=chosenOptionCategory, module=chosenOptionModule)
    questionBank = loadedModuleBank[0]
    answerBank = loadedModuleBank[1]

    print(questionBank[0])
    response = input("?: ")
    if response == answerBank[0]:
        print("correct")
    else:
        print("wrong!")



create_question_bank()