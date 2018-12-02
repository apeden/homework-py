"""
Created on Thu Sep  6 00:43:27 2018

@author: Alex Peden
"""

import random
from generic_homework import *

homeworkTasks = {"1":Addition,
                "2":EquivalentToFifth,
                "3":EquivalentToThreeFifths,
                "4":DevideByTen,
                "5":CakesByTen,
                "6":Spelling,
                "7":Sentence}
student_name = ""
date =""

things = (
"sensibly", 
"probably",
"horribly",
"invisible",
"miserable",
"possible",
##"uncle",
##"thankful",
##"wonderful,
##"beautiful",
##"helpfully",
##"painfully"
)

num_questions = len(things)


def inputRequest(request):
    userInput =""
    while userInput == "":
        userInput = input('\n\nWhat\'s' + request+ "? ")
        print("Please write something for" + request)
    return userInput
        
student_name = inputRequest(" your name")
date = inputRequest(" today\'s date.")


def homeworkSelection():   
    selection = None
    while selection == None:
        try:
            for key, value in homeworkTasks.items():
                print(key+": " + str(value.__name__))
            i = input("Select the homework task you would like \
to perform from this list: ")         
            selection = homeworkTasks[i] 
            return selection
        except KeyError:
            print("Enter a number between 1 and 7")
    


homework_task  = homeworkSelection()
print(homework_task)

if not (homework_task == Sentence, Spelling):
    num_questions = 10
    things = (1,10)

work = Session(student_name, num_questions, homework_task, date, things)
work.run_task()

