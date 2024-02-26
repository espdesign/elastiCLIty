import json
import random

def cls():
    print('\n'*100)

def load_json():
    f = open('modules.json')
    data = json.load(f)
    f.close()
    return data
            
def list_categories():
    categoriesList = []
    for i in load_json().keys():
        categoriesList.append(i) 
    return categoriesList

class JSONBank:
    def __init__(self) -> None:
        self.fullDict = load_json()
        self.categories = list_categories()
        self.modules = []
        
    def load_modules_from_category(self, argCategory):
        """
        Return list of modules in a chosen category
        """
        # modulesList = []
        data = load_json()
        for i in data[argCategory]:
            self.modules.append(i)
        # return modulesList
    def is_valid_input(self, isCat, argCM):
        if isCat is True:
            if argCM in self.categories:
                return True
            else:
                return False
        else:
            if argCM in self.modules:
                return True
            else:
                return False


class QuestionAnswersBank():
    def __init__(self) -> None:
        self.module = []
        self.moduleDict = {}

        self.answers = []
        self.questions = []

    def import_module(self, argCategory, argModule):
        self.module = argModule
        self.moduleDict = Databank.fullDict[argCategory][argModule]
        
        for question, answer in self.moduleDict.items():
            self.answers.append(answer)
            self.questions.append(question)
    
    def get_answer_from_index(self, argIndex):
        return self.answers[argIndex]
    
    def get_question_from_index(self, argIndex):
        return self.questions[argIndex]
    
        
class Question():
 

    def __init__(self) -> None:
        self.index = random.randint(0, len(QA_Bank.answers) - 1)
        self.answer = QA_Bank.answers[self.index]
        self.text = QA_Bank.questions[self.index]
        self.hasAnsweredCorrectly = False



    # def get_from_index(self, argIndex):
    #     pass
    def print_question_text(self):
        print(self.text, end=" $ ")
        return

Databank = JSONBank()
QA_Bank = QuestionAnswersBank() 

def main_menu():
    ## Display the category list
    print(Databank.categories)
    
    ## Display the module list from category chosen
    category_input = input("Please choose a category: ")

    validInputCategory = False
    while validInputCategory is False:
        if Databank.is_valid_input(True, category_input) is False:
            print("Error: Category does not exist.")
            category_input = input("Please choose a category: ")
        else:
            validInputCategory = True

    Databank.load_modules_from_category(category_input)
    print(Databank.modules)

    ## Load Questions and Answers Into QA_Bank from module chosen
    module_input = input("Please choose a module: ")

    validInputModule = False
    while validInputModule is False:
        if Databank.is_valid_input(False, module_input) is False:
            print("Error: Module does not exist.")
            module_input = input("Please choose a category: ")
        else:
            validInputModule = True
    QA_Bank.import_module(category_input, module_input)

    # TODO Create menu system for different modules

    def study(previousQuestionIndex = None):
        """Gamemode to study without scoring, just a random fast question prompt.

        Args:
            previousQuestionIndex (integer containing index of previous question, optional):. Defaults to None.
        """

        if previousQuestionIndex is not None:
            cur_loaded_question = Question()
            while cur_loaded_question.index == previousQuestionIndex:
                cur_loaded_question = Question()
        else:
            cur_loaded_question = Question()

        cur_loaded_question.print_question_text()
        player_answer = input()

        while cur_loaded_question.hasAnsweredCorrectly is False:
            index = int(cur_loaded_question.index) 
            correct_answer = QA_Bank.get_answer_from_index(index)

            if player_answer == correct_answer:
                cls()
                print("Correct!")
                cur_loaded_question.hasAnsweredCorrectly = True
                study(cur_loaded_question.index)

            elif player_answer == "exit":
                break
            else:
                cls()
                print(f"Incorrect. The correct answer is: {correct_answer}")
                cur_loaded_question.print_question_text()
                player_answer = input()
            
    study()

                 
main_menu()
print("Thanks for playing!")