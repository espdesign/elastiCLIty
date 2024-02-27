import json
import random

def cls():
    print('\n'*100)

def load_json():
    f = open('modules.json')
    data = json.load(f)
    f.close()
    return data

class DataBank:
    def __init__(self) -> None:
        self.allData = load_json()
        self.modules = []

        self.categories = []
        for i in self.allData.keys():
            self.categories.append(i)
        
        self.questions = []
        self.answers = []

    def load_questions_and_answers(self, categoryArg, moduleArg):
        """load questions and answers from category and module choices

        Args:
            categoryArg (string): the chosen category
            moduleArg (string): the chosen module
        """
        self.moduleDict = self.allData[categoryArg][moduleArg]
        
        for question, answer in self.moduleDict.items():
            self.answers.append(answer)
            self.questions.append(question)

    def load_module(self, categoryArg):
        """load a module from a chosen category

        Args:
            categoryArg (string): a chosen category from input
        """
        for i in self.allData[categoryArg]:
            self.modules.append(i)
        
    def is_exists(self, isCategory, arg):
        """check to see if data exists inside the DataBank

        Args:
            isCategory (bool): is the requested check a category?
            arg (string"): the name of category or module

        Returns:
            bool: if the requested item exists returns True or False
        """
        if isCategory is True:
            if arg in self.categories:
                return True
            else:
                return False
        else:
            if arg in self.modules:
                return True
            else:
                return False

class Menu():
    def __init__(self) -> None:
        self.chosenCategory = ""
        self.chosenModule = ""
        self.validInputCategory = False
        self.validInputModule = False

        self.menuLevel = "category"
    
    def category_choice(self, categoryArg):
        self.chosenCategory = categoryArg

    def module_choice(self, moduleArg):
        self.chosenModule = moduleArg
    

class QuestionEntry():
    """has 
    index = int \n
    answer = string \n
    questiontext = string \n
    hasAnsweredCorrectly = bool
    """
    def __init__(self) -> None:
        self.index = random.randint(0, len(DATA.answers) - 1)
        self.answer = DATA.answers[self.index]
        self.question = DATA.questions[self.index]
        self.hasAnsweredCorrectly = False
        self.playerAnswer = ""

    def print_question_text(self):
        print(self.question, end=" $ ")
        return
    
    def get_question_from_index(self, argIndex):
        self.index = argIndex
        self.answer = DATA.answers[argIndex]
        self.question = DATA.questions[argIndex]
        self.hasAnsweredCorrectly = False

    
class Display():
    def __init__(self) -> None:
        self.promptSymbol = " $ "

    def for_category(self):
        tmp = input(f"Please choose a category.{self.promptSymbol}")
        return tmp
    def for_module(self):
        tmp = input(f"Please choose a module.{self.promptSymbol}")
        return tmp
    def error_does_not_exist(self, inputArg, section):
        """display "inputArg" does not exist in "arg", please try again

        Args:
            inputArg (string): arg that was not found
            arg (string): name of section looking in
        """
        print(f"'{inputArg}' does not exist in {section}, please try again...")
    def for_answer(self):
        tmp = input(f"{self.promptSymbol}")
        return tmp


### Create Objects
DATA = DataBank()
MainMenu = Menu()
Prompt= Display()

## Main Logic For Games
def main():

    while MainMenu.menuLevel == "category":
        print(DATA.categories)
        while MainMenu.validInputCategory is False:
            currentInput = Prompt.for_category()

            if DATA.is_exists(True, currentInput) is False:
                cls()
                Prompt.error_does_not_exist(currentInput, "Categories")
                print(DATA.categories)
            else:
                MainMenu.validInputCategory = True
                cls()
                MainMenu.menuLevel = "module"
                MainMenu.chosenCategory = currentInput
                DATA.load_module(MainMenu.chosenCategory)
                print(MainMenu.chosenCategory)

    while MainMenu.menuLevel == "module":
        cls()
        print(DATA.modules)
        while MainMenu.validInputModule is False:
            currentInput = Prompt.for_module()

            if DATA.is_exists(False, currentInput) is False:
                cls()
                Prompt.error_does_not_exist(currentInput, "Modules")
                print(DATA.modules)
            else:
                MainMenu.chosenModule = currentInput
                MainMenu.validInputModule = True
                cls()                
                MainMenu.menuLevel = "none"
                studyGame()

def studyGame(questionIndex = None):
    """A gameMode that just randomy chooses a question, if answered incorrectly, 
    prompts for same question again.

    Args:
        questionIndex (int, optional): index for question that was answered wrong. Defaults to None.
    """
    
    DATA.load_questions_and_answers(MainMenu.chosenCategory, MainMenu.chosenModule)
    StudyQuestionEntry = QuestionEntry()

    if questionIndex is not None:
        StudyQuestionEntry.get_question_from_index(questionIndex)

    print(StudyQuestionEntry.question, end="")
    StudyQuestionEntry.playerAnswer = Prompt.for_answer()

    if StudyQuestionEntry.playerAnswer == StudyQuestionEntry.answer:
        cls()
        print("Correct!")
        studyGame()
    else:
        cls()
        print(f"'{StudyQuestionEntry.playerAnswer}' is incorrect.\nThe correct answer is {StudyQuestionEntry.answer}")
        studyGame(StudyQuestionEntry.index)



main()
