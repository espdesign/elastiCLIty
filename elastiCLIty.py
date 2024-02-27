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
        self.answerKey = DATA.answers[self.index]
        self.text = DATA.questions[self.index]
        self.playerInput = ""

        self.hasAnsweredCorrectly = False
        self.multipleAnswersExist = False
        self.isFirstRun = True

        if isinstance(self.answerKey, list):
            self.multipleAnswersExist = True


    def is_answer_correct_list(self, argAnswerInput):
        """If Input exists in answer list sets self.hasAnsweredCorrectly to True.

        Args:
            argAnswerInput (answer input): the players answer to the question
        """
        for i in self.answerKey:
            if argAnswerInput == i:
                self.hasAnsweredCorrectly = True

    def print_question_text(self):
        print(self.text, end=" $ ")
        return
    def get_question_from_not_index(self, argIndex):
        while self.index == argIndex:
            self.index = random.randint(0, len(DATA.answers) - 1)
            self.answerKey = DATA.answers[self.index]
            self.text = DATA.questions[self.index]

    def get_question_from_index(self, argIndex):
        self.index = argIndex
        self.answerKey = DATA.answers[argIndex]
        self.text = DATA.questions[argIndex]
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

    ## While loop checking for valid category input
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
    ## While loop checking for valid module input
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

def studyGame():

    def get_new_question(index = None):
        StudyQuestionEntry = QuestionEntry()
        if index is None:
            return StudyQuestionEntry
        else:
            StudyQuestionEntry.get_question_from_not_index(index)
            return StudyQuestionEntry

    def first_init():
        DATA.load_questions_and_answers(MainMenu.chosenCategory, MainMenu.chosenModule)
        question_loop()
    
    def question_loop(index = None):
        promptSymbol = " $ "

        if index is None:
            question = get_new_question()
        else:
            question = get_new_question(index)

        answerIsCorrect = False
        while answerIsCorrect is False:
            question.playerInput = input(f"{question.text}{promptSymbol}")
            answerIsCorrect = check_answer(question.playerInput, question.answerKey)
            if answerIsCorrect is True:
                answer_is_correct(question.index)
            else:
                answer_is_wrong(question.playerInput, question.answerKey)


    def answer_is_wrong(playerInput, answerKey):
        cls()
        print(f"Sorry, '{playerInput}' is not correct...")
        ## check to see if more than one answer exists for correct formatting of print statement
        if isinstance(answerKey, list):
            print(f"The correct answer is one of the following, {answerKey}")
        else:
            print(f"The correct answer is '{answerKey}'.")

    def answer_is_correct(index):
        cls()
        print("Correct!")
        question_loop(index)

    def check_answer(playerInput, answerKey):
        if isinstance(answerKey, list):
            # print("Answer is a list, checking against all possible answers...")
            for i in answerKey:
                # print(f"Checking player input{playerInput}: against {i}")
                if playerInput == i:
                    return True 
 
            return False
        else:
            if playerInput == answerKey:
                return True
            else:
                return False
    first_init()


main()