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

def loadcards(category):
    f = open('cards.json')
    data = json.load(f)
    f.close()
 
    for i in data[category]:
        for i in i:
            print(i)

    return(data[category])

loadcards("Linux")