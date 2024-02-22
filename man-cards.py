import json

def load_json():
    f = open('cardbank.json')
    data = json.load(f)
    f.close()
    return data
    
def list_categories():
    categories = []
    for i in load_json().keys():
        categories.append(i)
    return categories

def list_modules(chosenCategory):
    modulesList = []
    for i in chosenCategory.keys():
        modulesList.append(i)
    return modulesList

def load_chosen_category(input):
    data = load_json()
    return data[input]

def load_chosen_module(chosenCat, chosenMod):
    data = load_json()[chosenCat][chosenMod]
    return data


def main_menu():
    print(list_categories())
    # chosen_category = load_category(input("Pick a category: "))

    chosenCategory = input("Pick a category: ")
    moduleList = list_modules(load_chosen_category(chosenCategory))
    # after picking category and loading list of modules start the module_menu
    module_menu(moduleList, chosenCategory)



def module_menu(moduleList, chosenCategory):
    print(moduleList)
    chosenModule = input("Pick a module: ")
    moduleFinal = load_chosen_module(chosenCategory, chosenModule)
    print(moduleFinal)

# def list_modules(category):
#     data = load_json()
#     print(data[category])

    # for i in data[category]:
    #     modules.append(i)
    # return modules


main_menu()